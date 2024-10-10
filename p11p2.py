#Write a program that prompts the user for a non-negative integer and uses a while loop to
#calculate that number of terms of the Fibonacci Series. Try to make the program as small
#and efficient as possible.

#set f_0 and f_1 to 0 
#ask user to input a non-negative number (set this as limit)
#if the limit is a negative number, print out error message 
#else if limit equals 1, print f_0
#else if limit equals 2, print f_0 and f_1 
#else: 
    #set a to equal f_0 and b to equal f_1 
    #set i to 2 
    #while i is less than/equal to the limit:
        #fibonacci = b plus a 
        #print a comma, the fibonacci number and a blank space 
        #let a=b 
        #let b=fib 
        #increment i by 1 
#print that the program has finished 

f_0=0
f_1=1
limit = int(input('Enter the number of terms you want to calculate (an int > 0): '))

if limit <= 0:
    print('Error: Number entered was less than or equal to 0')
elif limit == 1:
    print('Series is:', f_0)
elif limit == 2:
    print('Series is: ', f_0, ', ', f_1, sep = '')
else:
    print('Series is: ', f_0, ', ', f_1, sep = '', end = '')
    a = f_0
    b = f_1
    i = 2
    while i < limit:
        fib = b + a
        print(',', fib, end = '')
        a = b
        b = fib
        i += 1
    print()
print('Finished!')