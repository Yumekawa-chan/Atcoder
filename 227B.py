n = int(input())
s = list(map(int, input().split()))
ls = set()
ans = 0

for i in range(1,200):
     for j in range(1,200):
          ls.add(4*i*j + 3*i + 3*j)

for el in s:
     if el not in ls:
          ans += 1

print(ans)