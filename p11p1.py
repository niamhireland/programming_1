#Writing code for a factorial that uses only two cases (based on code given in class)

#ask user to input a number 
#if number is less than or equal to 0, print a message to that effect and terminate the program
#else, set factorial and i to 1 
    #while i is less than/equal to number: 
        #multiply fact by i
        #increment i by 1 
    #print the resulting factorial 

number=int(input('Enter a number:'))

if number <=0:
    print('The factorial of 0 is 0. This program requires a number 0 or higher to function.')
else:
    fact=1
    i=1
    while i<=number:
        fact*=i
        i+=1
    print('Factorial of', number, 'is', fact)
