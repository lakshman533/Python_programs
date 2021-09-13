N=input()
def isprime(num):
    for i in range(2,num):
        if num%i==0:
            return('not prime')
        else:
            return('prime')
if len(N)>1:
    if len(N)%2==0:
        left=N[:len(N)//2]
        right=N[len(N)//2:]
    else:
        left=N[:len(N)//2]
        right=N[len(N)//2+1:]

l=isprime(int(left))
r=isprime(int(right))
if l=='prime' and r=='not prime':
    print("democratic prime")
else:
    print('not a democratic prime')
