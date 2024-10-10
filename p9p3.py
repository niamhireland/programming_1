#Write a program that prompts the user for a positive integer 
#Use a for loop to calculate the factorial of that number 

#request user input of positive number. 
#if negative number entered, program terminates 
#else:
    #if 1 or 0 is entered, set fact to be 1 
    #else: 
        #set fact to equal 1 
        #for i in range of 1 to number (increments of 1):
            #fact*=i
    #print the number that the user entered and the resulting factorial.
    #print 'Finished!'

number=int(input('Please enter a positive number:'))

if number<=0:
    print ('This program requires a positive integer to run.')
    print ('Finished!')
else:
    if number==0 or number==1:
        fact=1
    else:
        fact=1
        for i in range(1, number):
            fact*=i
    print ('Factorial of', number, 'is', fact, '.')
    print ('Finished!')