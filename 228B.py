n,x = map(int, input().split())
A = list(map(int, input().split()))

ans = 0

while(x != None):
     tmp = A[x-1]
     A[x-1] = None
     x = tmp
     ans += 1

print(ans-1)