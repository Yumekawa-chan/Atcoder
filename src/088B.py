n = int(input())
a = list(map(int, input().split()))
alice = []
bob = []

for i in range(n):
     if i % 2 == 0:# Aliceのターン
          alice.append(max(a))
     else: # Bobのターン
          bob.append(max(a))
     a[a.index(max(a))] = 0

print(sum(alice)-sum(bob))
