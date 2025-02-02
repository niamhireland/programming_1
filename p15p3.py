#Write a recursive function that takes as its single argument an integer ≥ 0 and prints out that number of terms from the 
#above series. In your function, include some print statements that allow you to see the operation of the recursion and 
#its progress towards the base cases.

#PSEUDOCODE
#define the function as x:
    #if x=0, print out that this has a value of 13. Return 13 
    #if x=1, print out that this has a value of 8. Return 8 
    #else
        #set recursive_result to be the function (x-2)
        #result equals recursive_result +13*(n-1)
        #print out the current value of f(x) to show progression to base    #using fstring to make code readable 
        #return result to the function
     

def function(x):
    if x==0:
        print ('0 is the base case and has a value of 13.')
        return 13
    if x==1:
        print ('1 is the base case and has a value of 8.')
        return 8
    else:
        recursive_result = function(x - 2)
        result=recursive_result + (13*(x-1))
        print(f'function({x}) = function({x - 2}) + 13 * ({x} - 1) = {recursive_result} + {13 * (x - 1)} = {result}')
        return result

#PSEUDOCODE 
#request user input of an int           #set this to be equal to x 
#if x is greater than/equal to 0
    #call the function 
    #print newline 
    #request repeat user input 
#else 
    #print that the user has entered a negative number and the program has terminated

x=int(input('Enter a positive integer (negative integer to quit):'))

if x>=0:
    print (function(x))
    print ()
    x=int(input('Enter a positive integer (negative integer to quit):'))
else:
    print ('You have entered a negative integer and this program has terminated')
    print ('Restart if you wish to continue.')