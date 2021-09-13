def rotatearr(a,n,k):
    a[:]=a[n-k:n]+a[0:n-k]
    return a

n=int(input("Please enter number of elements\n"))
a=list(map(int,input("enter the elements:").strip().split()))[:n]
k=int(input("enter a value"))
res=rotatearr(a,n,k)
str_res=[str(i) for i in res]
final_res=" ".join(str_res)
print(final_res)