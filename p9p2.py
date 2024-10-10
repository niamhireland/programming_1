#Write a program that prompts the user for a series of positive integers
#For each of the numbers entered, the program should calculate the sum of the numbers entered (up to and including that number) with a for loop.
#Program will stop when a negative number is entered. 

#user requested to enter a positive integer 
#while number is greater than 0:
    #for n in range zero to num 
    #add n to total
    #repeat until range is completed 
    #print result of adding all integers 
    #request new input from user 
#end program if num<=0

number=int(input('Enter the number that you wish to find the sum of all numbers in range for. Enter a negative number to exit.'))
total=0
while number>0:
    for n in range(1,number):
        total=total+n
    print('You entered '+ str(number) + '. The sum of the positive digits from 0 to this is: '+ str(total))
    number=int(input('Enter the number that you wish to find the sum of all numbers in range for. Enter a negative number to exit.'))

else:
    print('You have entered a negative number.')
    print ('Finished!')