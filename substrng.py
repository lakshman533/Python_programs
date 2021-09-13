n=input()
if len(n)>7 and len(n)%2!=0:
    print(n[(len(n)//2)-1:(len(n)//2)+2])
else:
    print("enter a valid odd numbered string")