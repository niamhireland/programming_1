#use a while loop to prompt a user for a series of numbers 
#check if each number is divisible by 2, 3, 5 or 7 and print out same. 
#program terminates if a negative number is entered

#user input of a positive integer 
#if a negative number is entered, program should read "Program is now terminated, please restart if you wish to continue."

#while the number is greater than 0:
    #if the number is evenly divisible by 2, print same 
    #if the number is not evenly divisible by 2, print same 
    #if the number is evenly divisible by 3, print same 
    #if the number is not evenly divisible by 3, print same 
    #if the number is evenly divisible by 5, print same 
    #if the number is not evenly divisible by 5, print same 
    #if the number is evenly divisible by 7, print same 
    #if the number is not evenly divisible by 7, print same 
    #request repeat user input of a positive integer to restart process 

print ('This program will assess whether a number is divisible by 2, 3, 5 or 7.')
number=int(input('Enter a positive integer. Enter a negative number to exit:'))

if number<=0:
    print('This program is now terminated, please restart if you wish to continue.')

while number>0:
    if number%2==0:
        print ('This number is evenly divisible by 2.')
    if number%2!=0:
        print ('This number is not evenly divisible by 2.')
    if number%3==0:
        print ('This number is evenly divisible by 3.')
    if number%3!=0:
        print ('This number is not evenly divisible by 3.')
    if number%5==0:
        print ('This number is evenly divisible by 5.')
    if number%5!=0:
        print ('This number is not evenly divisible by 5.')
    if number%7==0:
        print ('This number is evenly divisible by 7.')
    if number%7!=0:
        print ('This number is not evenly divisible by 7.')
    number=int(input('Enter a positive integer. Enter a negative number to exit:'))