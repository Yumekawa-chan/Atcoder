a,b = map(int, input().split())
length = len(str(min(a,b)))

a = str(a)
b = str(b)

for i in range(1,length+1):
     if int(a[-i]) + int(b[-i]) > 9:
          print("Hard")
          exit()
print("Easy")