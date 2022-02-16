import math

n = int(input())
x = []
y = []
lst = []

for i in range(n):
     x_,y_ = map(int, input().split())
     x.append(x_)
     y.append(y_)

for i in range(n):
     for j in range(i+1,n):
          leng = math.sqrt((x[i]-x[j])**2 + (y[i]-y[j])**2)
          lst.append(leng)

print(max(lst))