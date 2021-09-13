lst = []
sum=0
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())
    lst.append(ele)
for j in range(len(lst)):
    for k in range(j+1,len(lst)):
        if lst[j]==lst[k]:
            lst[k]=lst[k]+1
        else:
            break
total=0
for l in range(0,len(lst)):
    total=total+lst[l]
print(total)
