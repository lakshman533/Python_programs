text=input("Please enter the string\n")
count=1
length=""
if len(text)>=1:
    for i in range(0,len(text)-1):
        if text[i]==text[i+1]:
            count+=1
        else:
            length +=str(count)+","
            count=1
    length+=str(count)
else:
    print("please enter valid text")
l=length.split(",")
result=list(map(int,l))
print(result)

