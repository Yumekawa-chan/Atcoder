a,b,c,d = map(int, input().split())

def prime(s): # 素数だったら1を返す
     flag = False
     for i in range(2,s):
          num = s % i
          if num == 0:
               flag = True
               break

     if flag == False:
          return 1
     else:
          return 0

flg = False

for tk in range(a,b+1):
     flg = False
     for aok in range(c,d+1):
          if prime(tk+aok) == 1:
               flg = True
               break
     if flg == False:
          print("Takahashi")
          exit()

print("Aoki")
