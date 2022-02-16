s = input()
s_lst = []

for i in range(100000):
     s_lst.append("oxx")

s_lst = "".join(s_lst)
if s in s_lst:
     print("Yes")
else:
     print("No")