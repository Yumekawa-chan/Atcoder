n = input()
ans = 0

for i in range(1,int(n)+1):
     if "7" not in str(i): #10しんすう
          num = oct(i)
          if "7" not in str(num): #8しんすう
               ans += 1

print(ans)
