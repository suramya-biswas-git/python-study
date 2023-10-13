#Pan card’s id consists of alphanumerical figure. Length is always 10. Alphabets are in capital letters.
#You are required to accept a Pan card id then form a new string in such a way that the numbers in ascending order
#on the left hand side and alphabets are in descending order on the right hand side. If any alphabet is in lower case,
#it will be converted into upper case.

def panSort(pancard):
      digit=[]
      alpha=[]
      for stg in pancard :
         if stg.isdigit():
           digit.append(stg)

         if stg.isalpha():
           alpha.append(stg)

      digit.sort()
      alpha.sort(reverse=True)
      newpan=""
      for x in digit:
        newpan=newpan+x

      for x in alpha:
       newpan=newpan+x
      return newpan

    
panid=input("Enter a Pancard Id:")
if len(panid) !=10 :
    print("Sorry length should be 10")
    exit()
panid=panid.upper()
newpan=panSort(panid)
print(newpan)



