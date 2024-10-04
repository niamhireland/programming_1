#Program that takes as input a floating-point number 
#Prints out whether it is non-negative or not. 

number=float(input('Please enter a number:'))

if number <= 0:
    print (number, 'is a non-negative number.')
else:
    print (number, 'is a negative number.')