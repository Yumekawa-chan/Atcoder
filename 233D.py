n,k = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
for i in range(n):
     temp = a[i]
     if temp == k:
          ans += 1
     for j in range(i+1,n):
          temp += a[j]
          if temp == k:
               ans += 1
print(ans)
