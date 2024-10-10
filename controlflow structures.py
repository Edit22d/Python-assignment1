# control flow structures 
#Determines the order in which a program can be excesuted basing o the loops

#conditional statements
# These are statements that excesutes a specific or particure conditions
#create aprogram that asks a user for food types bought from the market
#The program should print :you bought chicken if the user enters chicken
# you bought liver if the user the enters liver,else the program should print fish
food_type = input('Enter the food types:')
if food_type == 'chicken':
    print(f'you bought chicken in the market:')
elif food_type =='liver':
    print(f'You bought liver in the market:') 
else:
    print(f'You bought fish in the market:')       
if food_type == 'chicken':
    print(f'You bought vchicken from the market:')
    #approach 2
if food_type !="chicken" or food_type != "liver" or food_type != "fish":
    print(f'Please choose from the above:')  
    #using logic operators
      