s=input()
vowels=['A','E','I','O','U']
k=0
st=0
for i in range(len(s)):
    if s[i] in vowels:
        k+=(len(s)-(i))
    else:
        st+=(len(s)-(i))
if k>st:
    print("Kevin",k)
elif st>k:
    print("Stuart",st)
else:
    print("Draw")