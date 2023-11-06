# Greets the user with "Hello World!".
print("Hello World!")

#Asks the user to input a number.
number = input("Enter a number: ")
 
#Converts the user's input to an integer. 
number = int(number) 

#Displays the number which was entered by the user back to them.
print("The numbered entered was", number) 

#If there is no remainder when the number is divided by 2, it is even.
if (number % 2) == 0:
#Tells the user that the number is even. 
    print("That is an even number") 
else: 
# Tells the user that their input is odd. 
    print("That is an odd number")
    
#If there is no remainder when the number is divided by 10, it is divisible by 10.
if (number % 10) == 0:
#Tells the user that the number is divisible by 10. 
    print("That is a number divisible by 10") 
else: 
# Tells the user that their input is not divisible by 10. 
    print("That is a number which is NOT divisible by 10.")