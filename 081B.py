n = int(input())
A = list(map(int, input().split()))
ans = 0
Flag = False

while Flag == False:
     for i in range(len(A)):
          if A[i]%2 != 0:
               Flag = True
               break
          A[i] = A[i]/2
     ans += 1

print(ans-1)