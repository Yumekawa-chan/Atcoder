n = int(input())
ans_box =[]

for b in range(80):
     a = n // 2**b
     c = n - a*2**b
     if a >= 0 and b >= 0 and c >= 0 and a*2**b+c == n:
          ans_box.append(a+b+c)

print(min(ans_box))