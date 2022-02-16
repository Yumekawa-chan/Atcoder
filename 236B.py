from collections import Counter

n = int(input())
a = list(map(int, input().split()))

for i,j in Counter(a).items():
     if j == 3:
          print(i)
