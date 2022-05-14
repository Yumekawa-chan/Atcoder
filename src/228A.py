s,t,x = map(int, input().split())

if s > t:
     if x < t:
          x += 24
     t += 24

if s <= x < t:
     print("Yes")
else:
     print("No")