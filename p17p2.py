#TASK

#Using your solution for the previous question as a guide, implement a optimised solution for calculating the
#common divisors of two numbers.


#PSEUDOCODE                 #utilising material from previous task as basis, as per instructions

#create function FindDivisors 
    #create tuple 'Divisors' to already contain 1, num1, num2
    #iterate through range - starting from 2, finishing on half the number +1 
        #if num1 and num2 can both be evenly divided by the current number in the range: 
            #add the current number to the list of divisors 
    #return divisor list 

#request user to input a positive number 
#repeat request for user to input a positive number 

#if either number is less than/equal to zero: 
    #print message that the numbers should be greater than 0. 
#else 
    #assign the functioncall the label 'commondivisors'
    #call the function and print result as part of a print statement
    #sum the common divisors and print same 
#print 'Finished!'

def findDivisors(num1, num2):
    """Finds the common divisors of num1 and num2
Assumes that num1 and num2 are positive integers
Returns a tuple containing the common divisors of num1 and num2"""
    divisors = (1, num1, num2)               #initialised divisor tuple to include 1, num1 and num2 as per task instructions
    for i in range(2, min(num1, num2)//2 + 1): #altered the range to start from 2 and only search to half the number (as per instructions)
        if num1 % i == 0 and num2 % i == 0:
            divisors += (i,)
    return divisors

number1 = int(input('Enter a positive integer: '))
number2 = int(input('Enter another positive integer: '))

if number1 <= 0 or number2 <= 0:
    print('Numbers should be > 0.')
else:
# First of all, get the common divisors and assign their values to commondivisors, then print out the results
    commondivisors = findDivisors(number1, number2)
    print(f'The common divisors of {number1} and {number2} are: {commondivisors}.')
#find sum of the divisors and print out 
    total=sum(findDivisors(number1, number2))
    print(f'Altogether, the common divisors total to: {total}.')
print('Finished!')