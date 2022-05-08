n,m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

for i in range(m):
     for j in range(len(A)):
          if B[i]==A[j]:
               A[j] = 0
               break
     if A.count(0) != i+1:
          print("No")
          exit()
          


print("Yes")