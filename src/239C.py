import math

def Euclid(a,b,c,d):
     return math.sqrt((a-c)**2 + (b-d)**2)

Lattice_Points_1 = []
Lattice_Points_2 = []

x1,y1,x2,y2 = map(int, input().split())


a = [x1+2,y1+1]
b = [x1+1,y1+2]
c = [x1+2,y1-1]
d = [x1+1,y1-2]
e = [x1-2,y1+1]
f = [x1-1,y1+2]
g = [x1-2,y1-1]
h = [x1-1,y1-2]
Lattice_Points_1.append(a)
Lattice_Points_1.append(b)
Lattice_Points_1.append(c)
Lattice_Points_1.append(d)
Lattice_Points_1.append(e)
Lattice_Points_1.append(f)
Lattice_Points_1.append(g)
Lattice_Points_1.append(h)

a = [x2+2,y2+1]
b = [x2+1,y2+2]
c = [x2+2,y2-1]
d = [x2+1,y2-2]
e = [x2-2,y2+1]
f = [x2-1,y2+2]
g = [x2-2,y2-1]
h = [x2-1,y2-2]
Lattice_Points_2.append(a)
Lattice_Points_2.append(b)
Lattice_Points_2.append(c)
Lattice_Points_2.append(d)
Lattice_Points_2.append(e)
Lattice_Points_2.append(f)
Lattice_Points_2.append(g)
Lattice_Points_2.append(h)

for point in Lattice_Points_1:
     if point in Lattice_Points_2:
          print("Yes")
          exit()
print("No")