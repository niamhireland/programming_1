#Write a recursive function that takes as its single argument an integer ≥ 1 and prints out that number of terms 
#from the given series. In your function, include some print statements that allow you to see the operation of
#the recursion and its progress towards the base case.

#PSEUDOCODE
#define the function as x:
    #if x=1
        #print message that this is the base case and return 1 
    #else 
        #set the recursive to be function(x-1)
        #result = recursive + 2*(x-1) 
        #print the function recurrance #(using f strings for simplicity and readability of code)
        #return result to the function 

def function(x):
    if x==1:
        print ('1 is the base case and has a value of 1.')
        return 1
    else:
        recursive_result = function(x - 1)
        result=recursive_result + 2*(x-1)
        print(f'function({x}) = function({x - 1}) + 2 * ({x} - 1) = {recursive_result} + {2 * (x - 1)} = {result}')
        return result
    
#(b) Write a program that prompts the user for a series of integers. For each number entered
#the program should check that it is greater than or equal to 1. If it is, it calls the
#function defined in part (a). The program should stop when a zero or a negative number
#is entered.

#PSEUDOCODE 

#request user input (inform user that a negative integer equals termination) #set user input = x
#if x is greater than 0
    #call the function 
    #print a newline 
    #request repeat user input 
#else 
    #print termination and restart message 

x=int(input('Enter a positive integer (negative integer to quit):'))

if x>0:
    print (function(x))
    print ()
    x=int(input('Enter a positive integer (negative integer to quit):'))
else:
    print ('You have entered a negative integer and this program has terminated')
    print ('Restart if you wish to continue.')