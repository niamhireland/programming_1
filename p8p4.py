#Use a while loop to prompt for a series of integers and check whether each number is in one of the specified ranges 
#Count the number of numbers in each range 

#while number is a positive number 
    #identify which range it falls into and add it to total count 
#once a negative number is entered, print the count for each range 

print ('This program takes a specific number and evaluates if it is in a specific range.')
print ('This program will also count the number of numbers in each range.')
number=int(input('Enter a positive integer. Enter a negative number to terminate:'))

equal_zero=0
one_twenty=0
twentyone_forty=0
fortyone_sixty=0
sixtyone_eighty=0
eightyone_hundred=0
more_than_hundred=0

while number>=0:
    if number==0:
        print ('This number is equal to 0. It has been added to your count total.')
        equal_zero+=1
        number=int(input('Enter a positive integer. Enter a negative number to terminate:'))
    if number>=1 and number<=20:
        print ('This number is in the 1-20 range. It has been added to your count total.')
        one_twenty+=1
        number=int(input('Enter a positive integer. Enter a negative number to terminate:'))
    if number>=21 and number<=40:
        print ('This number is in the 21-40 range. It has been added to your count total.')
        twentyone_forty+=1
        number=int(input('Enter a positive integer. Enter a negative number to terminate:'))
    if number>=41 and number<=60:
        print ('This number is in the 41-60 range. It has been added to your count total.')
        fortyone_sixty+=1
        number=int(input('Enter a positive integer. Enter a negative number to terminate:'))
    if number>=61 and number<=80:
        print ('This number is in the 61-80 range. It has been added to your count total.')
        sixtyone_eighty+=1
        number=int(input('Enter a positive integer. Enter a negative number to terminate:'))
    if number>=81 and number<=100:
        print ('This number is in the 81-100 range. It has been added to your count total.')
        eightyone_hundred+=1
        number=int(input('Enter a positive integer. Enter a negative number to terminate:'))
    if number>100:
        print ('This number is greater than 100. It has been added to your count total.')
        more_than_hundred+=1
        number=int(input('Enter a positive integer. Enter a negative number to terminate:'))
    if number<0:
        print ('This program requires a positive integer to function.')
        print ()
        print ('This is the sum of your entries to date.')
        print ('Number of entries which were equal to 0:', int(equal_zero))
        print ('Number of entries in the range 1-20:', int(one_twenty))
        print ('Number of entries in the range 21-40:', int(twentyone_forty))
        print ('Number of entries in the range 41-60:', int(fortyone_sixty))
        print ('Number of entries in the range 61-80:', int(sixtyone_eighty))
        print ('Number of entries in the range 81-100:', int(eightyone_hundred))
        print ('Number of entries that were greater than 100:', int(more_than_hundred))
        print ()
        print ('This program will now terminate, please restart if you wish to continue.')
