import numpy as np, trimesh as t
from trimesh.visual.material import PBRMaterial
from pathlib import Path
root=Path(__file__).resolve().parents[1]; scene=t.Scene()
colors={'metal':([105,111,117,255],.8,.26),'dark':([27,30,34,255],.2,.38),'pad':([44,45,49,255],0,.85),'driver':([160,166,170,255],.65,.35),'gold':([178,135,74,255],.75,.3)}
def add(name,m,pos,mat):
 c,metal,rough=colors[mat]; m.visual=t.visual.TextureVisuals(material=PBRMaterial(name=mat,baseColorFactor=c,metallicFactor=metal,roughnessFactor=rough)); scene.add_geometry(m,node_name=name,geom_name=name,transform=t.transformations.translation_matrix(pos))
def tube(points,r,segments=20):
 p=np.asarray(points); verts=[]; faces=[]
 for i,q in enumerate(p):
  tangent=p[min(i+1,len(p)-1)]-p[max(i-1,0)]; tangent/=np.linalg.norm(tangent); a=np.array([-tangent[1],tangent[0],0]); a/=np.linalg.norm(a); b=np.cross(tangent,a)
  for k in range(segments):
   th=2*np.pi*k/segments; verts.append(q+r*(np.cos(th)*a+np.sin(th)*b))
 for i in range(len(p)-1):
  for k in range(segments):
   a=i*segments+k;b=i*segments+(k+1)%segments;c=b+segments;d=a+segments;faces.extend([[a,b,c],[a,c,d]])
 return t.Trimesh(vertices=verts,faces=faces,process=False)
def oval(rx,ry,rz):
 m=t.creation.icosphere(subdivisions=3);m.apply_scale([rx,ry,rz]);return m
def disc(depth,ry,rz):
 m=t.creation.cylinder(radius=1,height=depth,sections=64);m.apply_transform(t.transformations.rotation_matrix(np.pi/2,[0,1,0]));m.apply_scale([1,ry,rz]);return m
def ring():
 # elliptical torus in YZ plane
 v=[];f=[];n=64;k=16
 for i in range(n):
  a=2*np.pi*i/n
  for j in range(k):
   b=2*np.pi*j/k;v.append([.11*np.sin(b),(.48+.105*np.cos(b))*np.cos(a),(.35+.095*np.cos(b))*np.sin(a)])
 for i in range(n):
  for j in range(k):
   a=i*k+j;b=i*k+(j+1)%k;c=((i+1)%n)*k+(j+1)%k;d=((i+1)%n)*k+j;f.extend([[a,b,c],[a,c,d]])
 return t.Trimesh(vertices=v,faces=f,process=True)
angles=np.linspace(.02,np.pi-.02,70)
add('Headband',tube([(1.03*np.cos(a),.35+1.26*np.sin(a),0) for a in angles],.105),[0,0,0],'metal')
angles=np.linspace(.43,np.pi-.43,50)
add('Headband_Cushion',tube([(.96*np.cos(a),.35+1.17*np.sin(a),0) for a in angles],.10),[0,0,0],'pad')
for side,s in [('Left',-1),('Right',1)]:
 add(side+'_Hinge',oval(.12,.22,.12),[s*1.02,.38,0],'metal')
 add(side+'_EarCup',disc(.22,.57,.43),[s*1.03,-.18,0],'dark')
 add(side+'_Outer_Shell',oval(.13,.57,.43),[s*1.19,-.18,0],'metal')
 add(side+'_Speaker_Driver',disc(.085,.39,.31),[s*.88,-.18,0],'driver')
 add(side+'_Driver_Core',disc(.045,.18,.18),[s*.825,-.18,0],'gold')
 add(side+'_Ear_Cushion',ring(),[s*.74,-.18,0],'pad')
add('Battery',t.creation.box(extents=[.075,.32,.23]),[1.11,-.18,0],'gold')
for i in range(3):add('Control_Button_'+str(i+1),oval(.035,.045,.08),[1.19,-.55+i*.11,.31],'dark')
scene.export(root/'public/models/nuno.glb')
print(len(scene.geometry), 'meshes')
