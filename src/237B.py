import numpy as np

h,w = map(int, input().split())
A = []

for i in range(h):
     a_ = list(map(str, input().split()))
     A.append(a_)
A = np.array(A)

B = np.transpose(A)
B = B.tolist()

for i in range(len(B)):
     B_ = " ".join(B[i])
     print(B_)