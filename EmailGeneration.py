#Due to epidemic situation , online classes are taking place for TSR School in the city.
#The school authority creates mail account for every student for providing study material, conduct examination,
#submission of projects etc. The mail id follows the rule- if the student name is Tracy Williams then mail id will be
#tracy.williams@tsr.edu . Or for student name is Mary Ann Milton, mail id will be mary.ann.milton@tsr.edu .

studentName=input("Enter Student Name:")
studentName=studentName.lower()
email=""
for x in studentName :
    
    if x==" " :
      email=email+"."
    else:
        email=email+x

email=email+"@tsr.edu"
print(email)
    
