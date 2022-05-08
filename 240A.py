a,b = map(int, input().split())

if abs(a-b) == 9 or abs(a-b) == 1:
     print("Yes")
     exit()
print("No")