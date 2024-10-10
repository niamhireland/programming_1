#Write a program that prompts the user for a positive integer 
#Use a while loop to calculate the sum of the positive integers up to and including that number 

#number = int(user input)
#initialise count to 0
#if number is less than 0
    #print ('This program requires a positive integer to run.')
    #print ('Finished!')

#else while count is less than or equal to number:
    #total=0 
    #total=count+total 
    #increment count by 1

number=int(input('Please enter a positive integer:'))
count=0

if number<0:
    print ('This program requires a positive integer to run.')
    print ('Finished!')

else: 
    total=0
    while count<=number:
        total=total+count
        count+=1
    print ('The sum of the positive integers up to and including this number is:', total)