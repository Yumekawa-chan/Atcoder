import math

A = input()

if 0<= int(A[-1]) <=2:
    print(str(math.floor(int(A)))+"-")
elif 3<= int(A[-1]) <=6:
    print(str(math.floor(int(A))))
else:
    print(str(math.floor(int(A)))+"+")


