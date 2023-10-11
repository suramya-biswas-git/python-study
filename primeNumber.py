n=int(input("Enter a whole number:"))
flag=True
for i in range(2,n):
    if (n%i)==0:
        flag=False
        break
    

if(flag==True):
    print(n,"is a Prime number")
else :
    print(n, "is not a Prime number")

      
