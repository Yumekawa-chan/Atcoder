from collections import Counter

n= int(input())
a = list(map(str, input().split()))
#a = list("".join(set(a)))

print(len(Counter(a).values()))
