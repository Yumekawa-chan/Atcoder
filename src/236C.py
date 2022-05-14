N,M = map(int, input().split())
S = list(map(str, input().split()))
T = list(map(str, input().split()))
cnt = 0
for i in range(N):
     if S[i] == T[cnt]:
          print("Yes")
          cnt += 1
     else:
          print("No")