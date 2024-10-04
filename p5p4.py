#Program taking integer as input 
#Printing different messages depending on whether the number is in range 0-20, 20-40, 40-60, 60-80, 80-100, >100 or =0.
#Program should print a message if the number entered is <0.

number=int(input('Please enter a number:'))

if (number)==0:
    print (number, 'you have entered the number zero.')
elif 0<number and number<20:
    print (number, 'is greater than 0 and less than or equal to 20.')
elif 20<number and number<40:
    print (number, 'is greater than 20 and less than or equal to 40.')
elif 40<number and number<60:
    print (number, 'is greater than 40 and less than or equal to 60.')
elif 60<number and number<80:
    print (number, 'is greater than 60 and less than or equal to 80.')
elif 80<number and number<100:
    print (number, 'is greater than 80 and less than or equal to 100.')
elif 100<number:
    print (number, 'is greater than 100.')
elif number < 0:
    print (number, 'is less than zero.')