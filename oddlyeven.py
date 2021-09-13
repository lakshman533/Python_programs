n=input()
odd=0
even=0
for i in range(len(n)):
    if i%2==0:
        even= even+ int(n[i])
    else:
        odd = odd + int(n[i])
sum=abs(even-odd)
print(sum)

