import math

N,A,B = map(int, input().split())

block = ""
# aは縦、bは横

if N % 2 == 0:
     for i in range(1,N+1):
          if i % 2 == 0:
               for n in range(N//2):
                    for a in range(A):
                         for n in range(N//2):
                              for b in range(B):
                                   block += "."
                              for b in range(B):
                                   block += "#"
                         for b in range(B):
                              block += "."        
                    print(block)
                    block = ""
          else:
               if i % 2 == 0:
                    for n in range(N//2):
                         for a in range(A):
                              for n in range(N//2):
                                   for b in range(B):
                                        block += "#"
                                   for b in range(B):
                                        block += "."
                              for b in range(B):
                                   block += "#"        
                         print(block)
                         block = ""
else:
          for i in range(1,N+1):
               if i % 2 == 0:
                    for n in range(N//2):
                         for a in range(A):
                              for n in range(N//2):
                                   for b in range(B):
                                        block += "."
                                   for b in range(B):
                                        block += "#"
                              for b in range(B):
                                   block += "."        
                         print(block)
                         block = ""
          else:
               if i % 2 == 0:
                    for n in range(N//2):
                         for a in range(A):
                              for n in range(N//2):
                                   for b in range(B):
                                        block += "#"
                                   for b in range(B):
                                        block += "."
                              for b in range(B):
                                   block += "#"        
                         print(block)
                         block = ""




