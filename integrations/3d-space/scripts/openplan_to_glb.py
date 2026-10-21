#!/usr/bin/env python3
"""Export an OpenPlan3D *web project JSON* to a basic architectural GLB.

Original adapter developed for chatgpt-toolkit. Does NOT run Blender addons.
Dependencies: numpy, trimesh, shapely. Units: OpenPlan3D cm -> GLB metres.
Supported: straight walls, rectangular door/window cutouts, floor polygons,
          columns and optional placeholder boxes for furniture.
Unsupported: curved/sloped walls, roofs, complex staircases, accurate BIM,
             decorative assets, photorealistic rendering or full app equivalence.
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np
import trimesh
from shapely.geometry import LineString
from shapely.ops import polygonize, triangulate, unary_union

CM = 0.01
_COLORS = {
    "wall": [232, 231, 225, 255],
    "floor": [194, 187, 170, 255],
    "column": [206, 208, 210, 255],
    "furniture": [131, 156, 166, 255],
}
# Approximate only: all proxy furnishings are visually recognizable boxes.
_FURNITURE_CM = {
    "sofa": (200, 90, 80), "chair": (80, 80, 90),
    "desk": (140, 70, 75), "coffee_table": (120, 60, 45),
    "table": (100, 60, 75), "bed_queen": (200, 150, 50),
    "bookshelf": (80, 30, 180), "wall_art": (80, 5, 60),
}


def _positive(v, label, nonnegative=False):
    if isinstance(v, bool) or not isinstance(v, (int, float)) or not math.isfinite(v) or (v < 0 if nonnegative else v <= 0):
        raise ValueError(f"{label} must be a finite {'non-negative' if nonnegative else 'positive'} number")
    return float(v)


def _point(p, label):
    if not isinstance(p, dict):
        raise ValueError(f"{label} must be a point")
    for axis in ("x", "y"):
        if axis not in p or isinstance(p[axis], bool) or not isinstance(p[axis], (int, float)) or not math.isfinite(p[axis]):
            raise ValueError(f"{label}.{axis} must be finite")
    return np.array([p["x"] * CM, -p["y"] * CM], dtype=float)


def _box(scene, key, dims, center, yaw=0, color=None):
    if min(dims) <= 1e-8:
        return
    box = trimesh.creation.box(extents=dims)
    mat = trimesh.transformations.rotation_matrix(yaw, [0, 0, 1]); mat[:3, 3] = center
    box.apply_transform(mat)
    box.visual.face_colors = color or _COLORS['wall']
    scene.add_geometry(box, geom_name=key)


def _add_segment(scene, key, p0, p1, thickness, zlo, zhi, color):
    delta=p1-p0
    length=float(np.linalg.norm(delta))
    if length <= 1e-6 or zhi-zlo <= 1e-6:
        return
    center=[float((p0[0]+p1[0])/2), float((p0[1]+p1[1])/2), (zhi+zlo)/2]
    _box(scene,key,[length,thickness,zhi-zlo],center,math.atan2(delta[1],delta[0]),color)


def _mesh_floor(scene, floor_id, lines, base_z, slab_thickness, count, warnings):
    """Triangulate simple enclosed regions from wall centre-lines. Approximate slab footprint."""
    if not lines: return count
    try:
        merged=unary_union([LineString([list(a), list(b)]) for a,b in lines])
        polys=list(polygonize(merged))
        seen=set()
        for idx, polygon in enumerate(polys):
            if polygon.area < 0.1: continue
            for tri in triangulate(polygon):
                if not polygon.covers(tri):continue
                v=np.array(tri.exterior.coords[:3],dtype=float)
                # preserve signed CCW orientation for clean normals
                if (v[1,0]-v[0,0])*(v[2,1]-v[0,1])-(v[1,1]-v[0,1])*(v[2,0]-v[0,0]) < 0:
                    v=v[[0,2,1]]
                verts=np.array([[*q, base_z-slab_thickness] for q in v]+[[*q,base_z] for q in v])
                faces=np.array([[3,4,5],[2,1,0],[0,1,4],[0,4,3],[1,2,5],[1,5,4],[2,0,3],[2,3,5]])
                mesh=trimesh.Trimesh(vertices=verts,faces=faces,process=True)
                mesh.visual.face_colors=_COLORS['floor']
                scene.add_geometry(mesh,geom_name=f"{floor_id}_slab_{count}");count+=1
        if not polys:warnings.append(f"{floor_id}: No closed wall contours; no floor slab generated")
    except Exception as exc:
        warnings.append(f"{floor_id}: Floor mesh generation failed: {exc}")
    return count


def convert(src: Path, dst: Path, proxies=False, slab=True):
    project=json.loads(src.read_text(encoding='utf8'))
    if not isinstance(project,dict) or not isinstance(project.get('id'),str) or not project['id'].strip():
        raise ValueError('Expected OpenPlan3D web project JSON with nonempty id')
    if not isinstance(project.get('floors'),list) or not project['floors']:
        raise ValueError('Expected floors[] (prepared RoomPlan JSON is not supported)')
    scene=trimesh.Scene()
    warnings=[];summary=defaultdict(int)
    ids=set()
    for floor in project['floors']:
        fid=floor['id']; level=floor.get('level',0)
        if fid in ids:raise ValueError(f'duplicate floor id {fid}')
        ids.add(fid)
        if not isinstance(floor.get('walls'),list):raise ValueError(f'{fid}: walls[] missing')
        zbase=float(floor.get('elevation',level*300))*CM
        floor_ids=set()
        def validate_id(item):
            id_=item.get('id')
            if not isinstance(id_,str) or not id_ or id_ in floor_ids:raise ValueError(f'{fid}: invalid or duplicate id: {id_}')
            floor_ids.add(id_)
        wall_by_id={}
        edges=[]
        for w in floor['walls']:
            validate_id(w);wid=w['id'];p0=_point(w['start'],wid+'.start');p1=_point(w['end'],wid+'.end')
            length=float(np.linalg.norm(p1-p0))
            if length <= 0.001:raise ValueError(f'{wid}: zero-length wall')
            thickness=_positive(w['thickness'],wid+'.thickness')*CM
            height=_positive(w.get('height',280),wid+'.height')*CM
            if w.get('curvePoint') is not None:
                raise ValueError(f'{wid}: curved walls unsupported (preventing inaccurate geometry)')
            if w.get('startHeight') is not None or w.get('endHeight') is not None:
                raise ValueError(f'{wid}: sloped walls unsupported')
            wall_by_id[wid]=(w,p0,p1,length,thickness,height)
            edges.append((p0,p1));summary['walls']+=1
        openings=defaultdict(list)
        for kind in ('doors','windows'):
            for op in floor.get(kind,[]):
                validate_id(op);wid=op.get('wallId')
                if wid not in wall_by_id:raise ValueError(f'{op["id"]}: unknown wallId {wid}')
                width=_positive(op['width'],op['id']+'.width')*CM
                p=float(op['position'])
                if not 0 <= p <= 1:raise ValueError(f'{op["id"]}: position not in [0,1]')
                wl=wall_by_id[wid][3]
                start=p*wl-width/2; end=p*wl+width/2
                if start < -1e-7 or end > wl+1e-7:
                    raise ValueError(f'{op["id"]}: opening extends beyond wall ends')
                zlo=(0 if kind=='doors' else _positive(op.get('sillHeight',90),op['id']+'.sillHeight',True))*CM
                zhi=zlo+_positive(op.get('height',210 if kind=='doors' else 120),op['id']+'.height')*CM
                if zhi>wall_by_id[wid][5]+1e-7:raise ValueError(f'{op["id"]}: opening taller than wall')
                openings[wid].append((start,end,zlo,zhi,op['id']))
                summary[kind]+=1
        for wid,(wall,p0,p1,length,thick,height) in wall_by_id.items():
            opens=sorted(openings.get(wid,[]))
            for a,b in zip(opens,opens[1:]):
                if b[0]<a[1]-1e-7:raise ValueError(f'{wid}: overlapping openings: {a[-1]} and {b[-1]}')
            bounds=sorted({0.,length,*[q for a,b,*_ in opens for q in (a,b)]})
            dir_=(p1-p0)/length
            for i,(a,b) in enumerate(zip(bounds,bounds[1:])):
                if b-a < 1e-6:continue
                mid=(a+b)*0.5;op=next((o for o in opens if o[0]<=mid<=o[1]),None)
                spans=[(0,height)] if op is None else [(0,op[2]),(op[3],height)]
                for j,(lo,hi) in enumerate(spans):
                    _add_segment(scene,f'{fid}_{wid}_{i}_{j}',p0+dir_*a,p0+dir_*b,thick,zbase+lo,zbase+hi,_COLORS['wall'])
        if slab:_mesh_floor(scene,fid,edges,zbase,0.06,0,warnings)
        for c in floor.get('columns',[]):
            validate_id(c)
            pos=_point(c['position'],c['id']+'.position')
            diameter=_positive(c['diameter'],c['id']+'.diameter')*CM
            height=_positive(c['height'],c['id']+'.height')*CM
            if c.get('shape','square')=='round':
                mesh=trimesh.creation.cylinder(radius=diameter/2,height=height,sections=32)
                mesh.apply_translation([pos[0],pos[1],zbase+height/2]);mesh.visual.face_colors=_COLORS['column']
                scene.add_geometry(mesh,geom_name=f'{fid}_{c["id"]}')
            else:_box(scene,f'{fid}_{c["id"]}',[diameter,diameter,height],[pos[0],pos[1],zbase+height/2],color=_COLORS['column'])
            summary['columns']+=1
        if proxies:
            for f in floor.get('furniture',[]):
                validate_id(f)
                pos=_point(f['position'],f['id']+'.position')
                dims=[float(f.get(k, _FURNITURE_CM.get(f.get('catalogId'),(50,50,50))[i]))*CM for i,k in enumerate(('width','depth','height'))]
                if min(dims)<=0:raise ValueError(f'{f["id"]}: invalid furniture dimensions')
                yaw=-math.radians(float(f.get('rotation',0)))
                _box(scene,f'{fid}_proxy_{f["id"]}',dims,[pos[0],pos[1],zbase+dims[2]/2],yaw,_COLORS['furniture'])
                summary['furniture_proxies']+=1
        elif floor.get('furniture'):
            warnings.append(f'{fid}: furniture omitted (use --furniture-proxies for placeholders)')
        if floor.get('stairs'):
            warnings.append(f'{fid}: stair geometry omitted (requires dedicated modeling)')
    if not scene.geometry:raise ValueError('No geometry produced')
    dst.parent.mkdir(parents=True,exist_ok=True)
    scene.export(str(dst),file_type='glb')
    audit={"source":str(src.name),"output":str(dst.name),"scene_bounds_m":np.round(scene.bounds,4).tolist(),"geometries":len(scene.geometry),"summary":dict(summary),"warnings":warnings,"limitations":["Floor slabs approximate centerline polygons","Doors and windows are openings without leaf/glazing detail","Materials are simple vertex colors, not photorealistic PBR","Curves, stairs and BIM semantics unsupported"]}
    dst.with_suffix('.audit.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2),encoding='utf8')
    return audit


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('input',type=Path,help='OpenPlan3D web-project JSON (centimetres)')
    p.add_argument('output',type=Path,help='Output .glb file')
    p.add_argument('--furniture-proxies',action='store_true',help='Include simple furniture placeholder boxes')
    p.add_argument('--no-floor',action='store_true',help='Do not infer floor slabs from closed contours')
    args=p.parse_args()
    try:
        result=convert(args.input,args.output,proxies=args.furniture_proxies,slab=not args.no_floor)
        print(json.dumps(result,ensure_ascii=False,indent=2))
    except (ValueError,KeyError,TypeError,ImportError) as exc:
        print('ERROR:',exc,file=sys.stderr);sys.exit(2)

if __name__=='__main__':main()
