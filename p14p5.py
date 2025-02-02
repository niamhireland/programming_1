#Write a recursive function that takes as its single argument a positive integer and prints out that number
#of terms from the Fibonacci Series. In your function, include some print statements that allow you to see the operation of
# the recursion and its progress towards the base cases.

#PSEUDOCODE
#Define function fib(x)
    # if x is 0, print message that this is the base case and return value 0
    #elif x is 1, print message that this is the base case and return values 0, 1
    #set up for the for loop: 
        #with fib1 equal to 0 and fib2 equal to 1 
        #extend fib sequence with fib1 and fib2 
        #print the term that the Fibonacci sequence will be calculated up to 
        #code enters for loop
            #for i in range (2, user's number)
            #let fibnum be the sum of fib1 and fib0
            #print message of same 
            #use multiple assign to set fib0=fib1 and fib1=fibnum
            #append fibnum to the sequence 
        #return fibonacci sequence 

def fib(x):
    if x == 0:
        print(f'fib(0) is the base case, returning 0')
        return [0]
    elif x == 1:
        print(f'fib(1) is the base case, returning [0, 1]')
        return [0, 1]
    
    fib1 = 0
    fib2 = 1
    fibonacci_sequence = [fib1, fib2]

    print(f'Calculating Fibonacci sequence up to term {x}:')

    for i in range(2, x):
        fibnum = fib1 + fib2
        print(f'fib({i}) = fib({i-1}) + fib({i-2}) = {fib1} + {fib2} = {fibnum}')
        fib1, fib2 = fib2, fibnum
        fibonacci_sequence.append(fibnum)

    return fibonacci_sequence

#Write a program that prompts the user for a series of integers. For each number entered the program
#should check that it is non-negative. If it is, it calls the function defined in part (a). The program should
#stop when a non-positive number is entered.

#PSEUDOCODE 
#request user to enter a positive number, input a negative number to terminate 
#while loop: 
    #while user's number is greater than 0, call function and print return value 
    #print a newline 
    #request repeat user input 
#else (if user inputs a negative number)
    #print that the program requires a positive number to function 
    #print a termination message 

x=int(input('Enter a positive integer. Enter a negative number to terminate:'))

while x>0:
    print(fib(x))
    print ()
    x=int(input('Enter a positive integer. Enter a negative number to terminate:'))
else: 
    print ('This program requires a positive number to function.')
    print ('Restart if you wish to continue.')
