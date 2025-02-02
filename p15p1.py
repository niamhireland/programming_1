#Write a recursive function that takes as its single argument an integer ≥ 1 and prints out that number of terms from a 
#given function. In your function, include some print statements that allow you to see the operation of the recursion and 
#its progress towards the base case.

#PSEUDOCODE 
#define the function to be function(x)
    #define x=1, set the return value to be 2 and include a print statement of same 
    #else
        #create variable recursive_result to contain function(x-1)
        #print (x-1) has the value (recursive_result)
        #return x+recursive_result to the function 

def function(x):
    if x==1:
        print ('1 is the base case and has a value of 2.')
        return 2
    else:
        recursive_result = function(x - 1)
        print (x - 1, 'has the value', recursive_result)
        return x + recursive_result
    

#(b) Write a program that prompts the user for a series of integers. For each number entered
#the program should check that it is greater than or equal to 1. If it is, it calls the
#function defined in part (a). The program should stop when a zero or a negative number
#is entered.

#PSEUDOCODE 
#request user input of integer
#if user input is greater than 0: 
    #call and print function 
    #request repeat user input 
#else print that user has entered a negative integer and that the program will terminate. 

x=int(input('Enter a positive integer (negative integer to quit):'))

if x>0:
    print (function(x))
    print ()
    x=int(input('Enter a positive integer (negative integer to quit):'))
else:
    print ('You have entered a negative integer and this program has terminated')
    print ('Restart if you wish to continue.')