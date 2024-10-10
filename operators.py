# ASSIGNMENT
#we have the following student details and mark enter these details from the keyboard
#StudentName = Ritah Liz
#StudentNumber = SEP23/BCS/14
#programming = 78
#Data science = 89
#computer application = 55
# calculate the average mark and print the answer in three decimal places 
# solutions
student_name = input('Enter the student name :')
student_number = input('Enter the student number :')
programming = int(input('Enter the programming mark :'))
data_science =int(input('Enter the data science mark :'))
computer_application = int(input('Enter computer application mark :'))
total_mark = programming + data_science + computer_application
number_of_subjects =3
average_mark = total_mark / number_of_subjects
print(f'average of{student_name} and number is {student_number} and average is: {average_mark :.3f}')
#Write a program that converts celcius to fahrenheit. The program shuld ask the user to enter the temp in degrees celcius and then display the temp converted to fahrenheit degrees
celcius = int(input ('\enter the temperature in celcius degrees'))
fahrenheit = (celcius *1.8) + 32
print(f'{celcius} degrees ceclius is equal to: {fahrenheit} degrees fahrenheit')
# A car's 
miles_driven = float(input('\Enter number of miles :'))
gallons_used = float(input('Enter the gallons used'))
MPG =miles_driven / gallons_used
print('cars miles per gallons = ', MPG,end="\n\n")


