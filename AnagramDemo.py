#An anagram is a word or phrase formed by rearranging the letters of another word or phrase,
#using all the original letters exactly once.
#For example,  1.Silent and Listen  2. Schoolmaster and The classroom 3.Conversation = Voices rant on.
#
text1=input("Enter 1st text:")
text2=input("Enter 2nd text:")
text1=text1.lower()
text2=text2.lower()
stg=""
stk=""
for x in text1:
    if x==" ":
        continue
    else :
        stg=stg+x
for y in text2:
    if y==" ":
        continue
    else :
        stk=stk+y

ss1=''.join(sorted(stg))
ss2=''.join(sorted(stk))
if ss1==ss2 :
    print("Anagram")
else:
    print("Not")


