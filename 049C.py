import re
S = input()

if re.match("^(dream|dreamer|erase|eraser)+$",S):
     print("YES")
     exit()
print("NO")