n = int(input())
h = list(map(int, input().split()))
ans = h[0]
for i in range(n):
     if i != n-1:
          if h[i] == h[i+1]:
               ans = h[i]
               break
          elif h[i] > h[i+1]:
               ans = h[i]
               break
          elif h[i] < h[i + 1]:
               ans = h[i+1]
print(ans)