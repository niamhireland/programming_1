#Taking an integer as input, printing out message if number is negative 

number=int(input('Please enter a positive number:'))

if number < 0:
    print ('I wanted a positive number, you entered a negative number. Please try again.')
else:
    print ('I love positive numbers, thank you for giving me', number, '!')