#Write a program that prompts the user for a series of non-negative integers and, for each of
#the numbers entered, uses a for loop to calculate that number of terms of the Fibonacci
#Series. The program should stop when a negative number is entered.

#set f_0 to 0 and f_1 to 1 
#ask user for non-negative number input (this will be the limit)

#while limit is greater than 0:
    #if limit equals 1:
        #print 'Series is: f_0'
    #if limit equals 2:
        #print 'Series is: f_0, f_1'
    #else 
        #let a=f_0
        #let b=f_1
        #for i in range (2, limit)
            #fibonacci number = b + a 
            #print a comma, the Fibonacci number and a space 
            #let a = b 
            #let b=fib 
            #increment 1 
        #once for loop is complete, print a new line
        #ask for repeat user input 
#if limit is less than/equal to 0, print error message and exit 

f_0 = 0
f_1 = 1
limit = int(input('Enter the number of terms you want to calculate (an int > 0): '))

while limit>0:
    if limit == 1:
        print('Series is:', f_0)
    if limit == 2:
        print('Series is: ', f_0, ',', f_1, sep = '')
    else:
        print('Series is: ', f_0, ',', f_1, sep = '', end = '')
        a = f_0
        b = f_1
        for i in range(2, limit):
            fib = b + a
            print(',', fib, end = '')
            a = b
            b = fib
            i+=1
    print()
    limit = int(input('Enter the number of terms you want to calculate (an int > 0): '))
if limit <= 0:
    print('Error: Number entered was less than or equal to 0')
print()
print('Finished!')