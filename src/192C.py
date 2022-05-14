n,k = map(int, input().split())

def g1(m): # 大きい順
     lst = sorted(list(str(m)), reverse=True)
     return int("".join(lst))
     
def g2(m): # 小さい順
     lst = sorted(list(str(m)))
     return int("".join(lst))

def f(x): # f(x)
    return g1(x)-g2(x)

ai = n

for i in range(k):
     ai = f(ai)

print(ai)
     

