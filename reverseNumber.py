n=int(input("Enter a number:"))
m=0
while n > 0 :
    x=n%10
    #n=n//10
    n=int(n/10)
    m=m*10+x

print(m)
  
    
