# The volume of a sphere with radius r is (4/3)* pie* r**2. What is the volume of the sphere with radius 5.
#Make sure the program enters the radius from the keyboardand provide the answer in 2  decimal places.
#  answers
radius= int(input('Enter the radius of the sphere : \t'))
pie = float(input('Enter the pie of the sphere: \t'))
volume = (4/3)* pie * radius**2
print(f'The volume of the sphere of {radius} and {pie} is {volume:.2f}')


#qn2
#create a programto calculate the area of a triangle (1/2 * base * height).
#Base and height should be entered using the keyboard.
#answer
base = int(input('Enter the base of the triangle: \t'))
height = int(input('Enter the height of the triangle: \t'))
area = (1/2)*base*height
print(f'The area of the triangle of {base} and {height} is {area:}')

#qn3 
# WWITI has tasked you to automate a simple grading system.As a python student,write a programe using to display the 
#grades that the students will be receiving based on the mark scored in A subject.
#The grades are:
# 90% - 100% Grade is A
# 80% - 89% Grade is B
# 70% - 79% Grade is C
# 60% - 69% Grade is D
# 50% - 59% Grade is E
# < 50% Fail

#answers
mark = int(input('Enter the mark scored in the subjects: \t'))
if mark>=90 and mark<=100 :
    print('Grade is A') 
elif mark>=80 and mark<=89 :
    print('Grade is B')
elif mark>=70 and mark<=79 :
    print('Grade is C')
elif mark>=60 and mark<=69 :
    print('Grade is E')
else:
    print('Fail')  

#qn4
#WITI Academy is proposing a sacco to help students save their money.Design a
# platform that will do the following .
#Welcome to,WITI ACademy Sacco.
#1.Deposit Money
#2.Withdraw Money
#3.Check Balance
#Ensure if the student selects 1, money is deposited and the minimum deposit should be 1000.
#If the student selects 2,money should be withdrawn and a minimum withdraw is 500.if the student 
# selects 3, the account balance should be displayed. 
 # ANSWERS
def sacco_transaction ():
    balance = 0
    run = 1
    while run == 1:
        print("\n Welcome to,WITI Academy sacco.")
        print("1.Deposit Money.")
        print("2.Withdraw Money.")
        print("3.Check Balance.")
        
        student_choice = int(input("Please choose choice (1,2 or 3): "))
        if student_choice == 1:
            print(".......processing a deposit transaction....... ")
            deposit_amount = int(input("Enter the amount to be deposited:  "))
            if deposit_amount < 1000:
                print("Minimum amount is 1000")
            else:
                balance += deposit_amount
                print(f"Dear student you have successfully deposited and your new account balance is{balance: ,}")
        elif student_choice == 2:
            print(".........Processing a withdraw transaction..........")
            withdraw_amount = int(input("Enter the amount to be withdrawn:  "))
            if balance == 0:
                print("Your account balance is 0")
            elif withdraw_amount < 500:
                print("Minimum withdraw is 500")
            elif withdraw_amount > balance:
                print("Insufficient balance.")
            else:
                balance -= withdraw_amount
                print(f"Dear student you have sucessfully withdrawn and your account balance is {balance: ,}")
        elif student_choice == 3:
            print(f"Your account balance is {balance}")
        else:
            print("Invalid input,please choose options 1,2 or 3")
        
        run = int(input("Enter 1 to continue or any number to exit: "))
        if run != 1:
            print("Thank you for using our sacco.")
            break
sacco_transaction()        
               

        
        
        
    
    
    
     

    


