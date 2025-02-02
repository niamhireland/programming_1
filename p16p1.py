#TASK 
#Write a recursive function that takes as its single argument an integer ≥ 1 and prints out that
#number of terms from the above series.
#(b) Write a program that prompts the user for a series of integers. For each number entered the
#program should check that it is greater than or equal to 1. If it is, it calls the function defined
#in part (a). The program should stop when a zero or a negative number is entered.
#(c) In your function, include some print statements that allow you to see the operation of the
#recursion and its progress towards the base case.

#PSEUDOCODE 
#define the function (let the number = x)
    #if value of x is 1:
        #print that this is the base case and has a value of 2. 
        #return 2 as the value 
    #else 
        #set the recursive_result to equal function(x-1)
        #set result = 2 times (x-1)
        #print the recursion using fstrings for simplicity 
        #return result as the value 

#request user input of x as an int (stating to input a positive number and a negative number to terminate)

#evaluate if x is greater than or equal to 1
    #if it is, call the function 
    #print a blank line 
    #request repeat user input for x 
#else if x is less than 1 
    #print that the program requires a positive number to function 
    #print that program is now terminated 

def function(x):
    '''Finds the value of x in a recursive function, assumes that x is a positive number '''
    if x==1:
        print('1 is the base case and has a value of 2.')
        return 2
    else:
        recursive_result=function(x-1)
        result=2*(x-1)
        print(f'function({x}) = 2*function({x-1}) = 2* {recursive_result} = {result}')
        return result 
    

x=int(input('Enter a positive number. Enter a negative number to terminate:'))

if x>=1:
    function(x)
    print ()
    x=int(input('Enter a positive number. Enter a negative number to terminate:'))
else:
    print ('This program requires a positive number to function.')
    print ('This program has now terminated, restart if you wish to continue.')