#write a function that takes a non-negative integer and prints that number of terms of the Fibonacci series 

#Define function fib(x)
    #Let fib1=0 and fib2=1 
    #create a list named fibonacci_sequence 
    #if x is 0:
        #append fib1 to the fibonacci_sequence 
    #otherwise: 
        #extend the list by fib1 and fib2
        #set i to equal 2 and fibnum to equal 0 
        #use a for loop to iterate through the numbers in range (i to user's number)
            #let fibnum = fib1 plus fib2 
            #use multiple assign to change the values of fib1 and fib2 
                #fib1 now contains value from fib2, fib2 contains value from fibnum
            #increment i by 1 
            #append resulting fibnum to the fibonacci_sequence list 
    #return the results of the list when the function is called 

def fib(x):
    fib1 = 0
    fib2 = 1
    fibonacci_sequence = []

    if x == 0:
        fibonacci_sequence.append(fib1)
    elif x >= 1:
        fibonacci_sequence.extend([fib1, fib2])
        i = 2
        fibnum = 0
        for i in range(i, x):
            fibnum = fib1 + fib2
            fib1, fib2 = fib2, fibnum
            i += 1
            fibonacci_sequence.append(fibnum)
    return fibonacci_sequence

#b) Write a program that prompts the user for an integer and checks if the integer is non-negative. 
#If negative, prints out an error message. If non-negative, calls the function from part a) and prints out result

#PSEUDOCODE
#request user input of an integer
#if x is less than 0, print a message that the program requires a non-negative number 
#else print the entered integer and the number of terms in the Fibonacci sequence, up to and including that term.

x = int(input('Enter a non-negative integer: '))

if x<0:
    print('This program requires a non-negative number to function.')
else:
    print ('You entered', x, '. The number of terms in the Fibonacci sequence for this number are:', fib(x))
