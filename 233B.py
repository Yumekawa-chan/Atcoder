l,r = map(int, input().split())
s = input()

st1 = s[:l-1]
st2 = s[l-1:r]
st3 = s[r:]
st2 = st2[::-1]
#print(st1)
#print(st2)
#print(st3)
print(st1+st2+st3)
