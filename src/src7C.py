n = int(input())
s = []
t = []

for i in range(n):
     s_,t_ = input().split()
     s.append(s_)
     t.append(t_)

for i in range(n):
     for j in range(n):
          if i != j and s[i] == s[j] and t[i] == t[j]:
               print("Yes")
               exit()

print("No")