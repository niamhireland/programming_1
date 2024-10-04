#Program that takes as input a floating-point number 
#Prints out whether it is positive, negative or equal to 0. 

number=float(input('Please enter a number:'))

if number == 0:
    print ('You gave me 0! I love 0!')
elif number%2==0:
    print ('You gave me', number, '! Thank you for choosing a positive number!')
else:
    print (number, 'is a negative number. Thank you, I love negative numbers!')