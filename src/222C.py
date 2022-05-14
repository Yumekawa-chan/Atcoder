n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = []

for i in range(n):
     for j in range(a[i],b[i]+1):
          c.append(j)

print(c)
print(len(c))