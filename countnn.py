def repeat(n):
    a=[]
    while n!=0:
        ele = n%10
        if ele in a:
            return 0
        else:
            a.append(ele)
            n=n//10
    return 1
n=int(input())
m=int(input())
res=0
for i in range(n,m+1):
    res=res+repeat(i)
print(res)
