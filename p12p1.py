#a) write a function that takes as single argument a non-negative integer and returns the factorial

#PSEUDOCODE
#define fact(x)
    #initialise res to equal 1 
    #set the range to cover 1 to the user's input number+1
    #multiply res by i in the range 

def fact(x):
    if x>0:
        res=1
        for i in range(1, x+1):
            res*=i
    return res 

x=int(input('Enter a non-negative integer:'))

#b) write a program that prompts the user for an integer and checks whether the number is non-negative. 
#If negative, print out an error message. 
#If number is positive, call the function from a)

#PSEUDOCODE
#request user input (equating this to x)
#if x is greater than 0, print the factorial calculated by the function 
#else (if x is less than/equal to 0), print that the program can't complete the task

if x>0:
    print ('The factorial of', str(x), 'is', fact(x))
else:
    print ('This program requires a non-negative number to function.')

print ('Finished!')