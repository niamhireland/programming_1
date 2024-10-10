#prompt the user for a series of positive integers 
#for each of the numbers entered, calculate the factorial using a while loop 
#program should stop when a negative number is entered. 

#user input of positive number to find factorial of. 

#if the number is less than or equal to 0:
    #terminate the program and inform user that the program can only run with a positive integer

#else:
    #if the number is larger than 0, establish 'fact' to be 1. 'Fact' meaning starting digit for factorial.
    #if number equals 0 or 1, print out that the factorial of that number is 1. 
    #else 
        #initialise start_number to be the same as number (to ensure that initial number can be printed out accurately at the end)
        #while user input number is greater than/equal to 1:
            #Multiply the user entry by 'fact', letting fact take on the value of the result 
            #Subtract 1 from the user value 
            #Repeat until the loop defaults to false 
            #print initial number and resulting factorial before asking for new input. 

print('This program takes input of a positive integer and returns the factorial of said number.')
number=int(input('Enter a positive number to continue. Enter a negative number to exit.'))

if number<0:
    print ('This program requires a number larger than the one you have entered.')
    print ('This program will now terminate.')
else:
    while number>=0:
        fact=1
        if number==0:
            print ('You have entered 0. The factorial of 0 is 1.')
            number=int(input('Enter a positive number to continue. Enter a negative number to exit.'))
        elif number<0:
            print ('This program requires a number larger than the one you have entered.')
            print ('This program will now terminate.')
        elif number==1:
            print ('You have entered 1. The factorial of 1 is 1.')
            number=int(input('Enter a positive number to continue. Enter a negative number to exit.'))
        else: 
            start_number=number
            while number>=1:
                fact=number*fact
                number=number-1
            print ('The factorial of '+str(start_number)+' is '+str(fact))
            number=int(input('Enter a positive number to continue. Enter a negative number to exit.'))