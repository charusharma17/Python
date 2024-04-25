#Voting system
name=input("Enter your name")
age=int(input("Enter your age"))
if(age>=18):
    print("You are eligible for voting")
    print("Make your choice")
    print('Press : 1 for BJP ; 2 for INC ; 3 for AAP ; 4 for BSP ; 5 for RJD')
    choice=int(input("Enter your Choice"))
    if(choice==1):
        print("you voted for BJP")
    elif(choice==2):
        print("you voted for INC")
    elif(choice==3):
        print("you voted for AAP")
    elif(choice==2):
        print("you voted for BSP")
    elif(choice==2):
        print("you voted for RJD")
    else:
        print("Invalid Choice")
else:
    print("You are not eligible for vote")
