n=input().lower()
m=input().lower()
n=n.replace(" ","")
m=m.replace(" ","")
for i in n:
    for j in m:
        if i==j:
            n=n.replace(i,"",1)
            m=m.replace(i,"",1)
            break
count=len(n+m)
f=['Friends','Lovers','Affection','Marriage','Enemies','Siblings']
if count>0:
    while len(f)>1:
        c=count%len(f)
        index=c-1
        if index>=0:
            str1=f[:index]
            str2=f[index+1:]
            f=str2+str1
        else:
            f=f[:len(f)-1]
    print(f[0])
else:
    print("proper name please")

