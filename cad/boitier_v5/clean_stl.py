# -*- coding: utf-8 -*-
# Garde uniquement le plus gros solide d'un STL ASCII (retire les micro-fragments).
# Usage: python clean_stl.py fichier.stl
import sys

def parse(path):
    facets=[]; cur=[]; normals=[]
    with open(path, errors="replace") as f:
        n=None
        for line in f:
            s=line.split()
            if not s: continue
            if s[0]=="facet":
                n=tuple(float(x) for x in s[2:5])
            elif s[0]=="vertex":
                cur.append((float(s[1]),float(s[2]),float(s[3])))
                if len(cur)==3:
                    facets.append((cur[0],cur[1],cur[2])); normals.append(n); cur=[]
    return facets, normals

def key(v): return (round(v[0],3),round(v[1],3),round(v[2],3))

def main(path):
    facets, normals = parse(path)
    parent={}
    def find(x):
        parent.setdefault(x,x); r=x
        while parent[r]!=r: r=parent[r]
        while parent[x]!=r: parent[x],x=r,parent[x]
        return r
    def uni(a,b):
        ra,rb=find(a),find(b)
        if ra!=rb: parent[ra]=rb
    for f in facets:
        a,b,c=key(f[0]),key(f[1]),key(f[2]); uni(a,b); uni(b,c)
    from collections import defaultdict
    groups=defaultdict(list)
    for i,f in enumerate(facets):
        groups[find(key(f[0]))].append(i)
    if len(groups)<=1:
        print("OK deja 1 seul solide (%d facettes)"%len(facets)); return
    biggest=max(groups.values(), key=len)
    keep=set(biggest)
    with open(path,"w") as o:
        o.write("solid cleaned\n")
        for i in keep:
            n=normals[i] or (0,0,0); f=facets[i]
            o.write("facet normal %g %g %g\n outer loop\n"%n)
            for v in f: o.write("  vertex %g %g %g\n"%v)
            o.write(" endloop\nendfacet\n")
        o.write("endsolid cleaned\n")
    print("nettoye : %d solides -> 1 (garde %d/%d facettes)"%(len(groups),len(keep),len(facets)))

if __name__=="__main__":
    main(sys.argv[1] if len(sys.argv)>1 else "v5_base.stl")
