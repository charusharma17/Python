#Grading system 
s1=int(input("Enter marks of 1st subject"))
s2=int(input("Enter marks of 1st subject"))
s3=int(input("Enter marks of 1st subject"))
s4=int(input("Enter marks of 1st subject"))
s5=int(input("Enter marks of 1st subject"))
marks=s1+s2+s3+s4+s5/100
p=(marks/500)*100
print(p,"is your percentage")
if(p<=100 and p>=90):
    print("Grade A")
elif(p<90 and p>=70):
    print("Grade B")
elif(p<70 and p>=50):
    print("Grade C")
elif(p<50 and p>=30):
    print("Grade D")
elif(p<30):
    print("Grade F")
else:
    print("Invalid Choice")

    

    

             
