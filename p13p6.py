#Write a recursive function that takes as its single argument a non-negative integer, have program return the factorial of the number.
#b) Write a program that prompts the user for an integer and checks that the number entered is non-negative.
#If it is, it calls the function defined in part (a) and prints out the result; if not, it prints out an appropriate error message.
#(c) In function, include some print statements that allow you to see the operation of the recursion and its progress towards the base case.

#PSEUDOCODE 
#define the function (x)
    #include a docstring stating that the function returns the factorial of a non-negative number, using recursive definition
    #if x=0:, return 1 
    #else:
        #let result = x times the factorial (x-1)
        #use an fstring to print: 
            #the factorial formula and result (f string to simplify the process, as otherwise would be a lot of concatenation)
            #repeat this to show recursion operating 
        #return the result 

#request user input of a positive integer 
#if user inputs number less than 0:
    #print error and termination messages 
#else print the factorial that results when function is called 
#print Finished!

def fact(x):
    """Function that returns the factorial of its argument
    Assumes that its argument is a non-negative integer
    Uses a recursive definition
    """
    if x == 0:
        return 1
    else:
        result = x*fact(x - 1)
        print(f"Factorial of ({x})={x}*fact({x - 1}) = {x}*{result}={x * result}")
        return result

x=int(input('Enter a non-negative number:'))

if x<0:
    print ('This program requires a non-negative number to function.')
    print ('Please restart if you wish to continue.')

else: 
    print ('The factorial of', x, 'is', fact(x))

print ('Finished!')