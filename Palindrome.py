str=input("Enter a word:")
stg=str[:0:-1]
stg=stg+str[0];
if str==stg :
    print("Palindrome")
else:
    print("Sorry")
