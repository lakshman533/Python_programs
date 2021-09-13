a = int(input())
n = a*(a+1)/2
lst =[]
i = 2
while i <= 2*n:
    lst.append(i*(2*i-1))
    i = i+2
lst1 = []
for j in lst:
   lst1.append(str(j))
lst2 = []
for k in lst1:
    lst2.append(k.zfill(5))
m = 0
n = 1
for l in range(a):
    output = ' '.join(lst2[m:n])
    print(output)
    m = n
    n = n+l+2