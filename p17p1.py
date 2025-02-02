#TASK

#Two suggested optimisations for the algorithm to calculate the divisors of a number are to initalise the divisors
#tuple to include 1 and the number itself and to only search from 2 and as far as half of the number. Revise
#the solution on Pages 14–17 of the slides to include these optimisations.
#investigate whether further optimisations can be made 


#PSEUDOCODE                 #utilising material from lecture 16 as a base, as per instructions

#create function FindDivisors 
    #create tuple 'Divisors' to already contain 1, num
    #iterate through range - starting from 2, finishing on half the number +1 
        #if num1 and num2 can both be evenly divided by the current number in the range: 
            #add the current number to the list of divisors 
    #return divisor list 

#request user to input a positive number 
#repeat request for user to input a positive number 

#if either number is less than/equal to zero: 
    #print message that the numbers should be greater than 0. 
#else 
    #print the divisors, using a function call 
    #using sum function to find the total of divisors 
#print 'Finished!'

def findDivisors(num):
    """Finds the divisors of num
Assumes that num is positive integer
Returns a tuple containing the divisors of num"""
    divisors = (1, num, )               #initialised divisor tuple to include 1, num as per task instructions
    for i in range(2, int(num)//2 + 1): #altered the range to start from 2 and only search to half the number (as per instructions)
        if num % i == 0:
            divisors += (i,)
    return divisors

num = int(input('Enter a positive integer: '))

if num <= 0:
    print('Number should be > 0.')
else:
# First of all, get the common divisors and print them out
    divisors = findDivisors(num)
    print('The divisors of', num, 'are:', divisors)
# Here is how I further optimised the code - I have used the sum function to find the total of all divisors
    total = sum(divisors)
    print ('Altogether, the divisors total to:', total)
print('Finished!')