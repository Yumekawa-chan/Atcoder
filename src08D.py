from collections import Counter
lst = list(map(int, input().split()))

for k,v in Counter(lst).items():
     if v == 3:
          print(k)
     elif v == 1:
          print(k)
