n = input()
leng = len(n)

if leng == 4:
     print(n)
elif(leng ==3):
     print("0"+n)
elif(leng == 2):
     print("00"+n)
else:
     print("000"+n)