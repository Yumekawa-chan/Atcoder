s1 = input()
s2 = input()

if s1 == "##" or s2 == "##":
     print("Yes")
     exit()

for i in range(2):     
     if s1[i] == "#" and s2[i] == "#":
          print("Yes")
          exit()

print("No")