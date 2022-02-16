n = int(input())
head = "AGC"

if n > 99:
     if n > 41:
          n += 1
          print(head + str(n))
     else:
          print(head+str(n))
elif(n < 10):
     if n > 41:
          n += 1
          print(head + "00" + str(n))
     else:
          print(head+ "00" +str(n))
else:
     if n > 41:
          n += 1
          print(head + "0" + str(n))
     else:
          print(head+ "0" +str(n))

