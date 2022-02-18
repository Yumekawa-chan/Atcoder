n = int(input())
a = list(map(int, input().split()))
box = []

for i in range(len(a)):
     for j in range(i,len(a)):
          if i != j:
               dif = abs(a[i]-a[j])
               box.append(dif)

print(max(box))