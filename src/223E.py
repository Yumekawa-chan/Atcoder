x = int(input())
ans = 0

for i in range(10**100 + 1):
     ans += int(x//10**i)
     if int(x//10**i) == 0:
          break
     
print(ans)
