stk=input("Enter a word:")
stg=stk[:0:-1]
stg=stg+stk[0];
stk=stk.lower()
stg=stg.lower()
if stk==stg :
    print("Palindrome")
else:
    print("Sorry")
