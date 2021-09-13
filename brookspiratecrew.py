P=int(input())
l=[]
for i in range(1,P+1):
    l.append(i)
print(l)
if len(l)>0:
    while len(l)>1:
        if len(l)%2==0:
            l=l[::2]
        else:
            right=l[len(l)-1:]
            left=l[:len(l)-1:2]
            l=right+left
    print(l[0])
else:
    print("no one's left to eat")