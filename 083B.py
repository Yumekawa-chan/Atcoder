n,a,b = map(int, input().split())
sum = 0

def kakuketanowa(n):
     wa = 0
     n = str(n)
     for i in range(len(n)):
          wa += int(n[i])
     return wa

for i in range(1,n+1):
     if a<=kakuketanowa(i)<=b:
          sum+=i

print(sum)

