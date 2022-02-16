x,y = map(int, input().split())
ans = 0
if x > y:
     print(0)
     exit()

while x < y:
     x += 10
     ans += 1

print(ans)