n = int(input())
a = list(map(int, input().split()))

box = []

for i in range(len(a)):
     box.append("-"+str(a[i])+"-")

box = "".join(box)

lit = ""
for k in range(2,max(a)):
     for i in range(k):
          lit += "-" + str(k) + "-"
     box.replace(lit,".")
     print(lit)
     lit = ""

print(box)