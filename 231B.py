n = int(input())
lst = []
num = 0

for i in range(n):
     s = input()
     lst.append(s)

for el in set(lst):
     if num < lst.count(el):
          num = lst.count(el)
          ans = el

print(ans)

