#TASK
#A perfect number is a positive integer that is equal to the sum of its proper factors (its positive
#integer factors excluding the number itself). For example, 6 (with proper factors 1, 2 and 3) and 28
#(with proper factors 1, 2, 4, 7 and 14) are perfect numbers. Write a program that prompts the user for 
#a positive integer and finds all the perfect numbers up to and including that number.

#PSEUDOCODE
#create a function FindPerfect to find the perfect numbers in range (1,x+1)         #x+1 to ensure range includes user's x input
    #initialise empty list to store perfect numbers 
    #for loop through 1-x:             #examining each number in the range 
        #initialise empty list to store divisors (separately for each number in the range)
        #using 'i' as a stand in for the number currently being iterated on 
        #for loop (1 - x)               #checking for divisors
            #using 'j' as stand in for number currently being iterated on
            #if number 'i' is evenly divisible by number 'j': 
                #add divisor (j) to list of stored divisor numbers 
            #calculate sum of all divisors found for the current number (so all the 'j's for a given 'i')
            #if divisor sum = number itself, add it (it meaning 'i') to the list of perfect numbers 
    #return list of perfect numbers 
    
def FindPerfect(x):
    """Assume that x is a positive integer
Find the perfect numbers in range 1-x
Print out the perfect numbers"""
    perfectnumbers=[]
    for i in range (1, x+1):
        divisors=[]
        for j in range (1,i):
            if i%j==0:
                divisors.append(j)
        if sum(divisors)==i:
            perfectnumbers.append(i)
    print (f'The perfect numbers in range 1-{x} are: {perfectnumbers}')
    return perfectnumbers

x=int(input('Enter a positive number. Enter a number<=0 to quit: '))

while x>0:
    FindPerfect(x)
    x=int(input('Enter a positive number. Enter a number<=0 to quit: '))
else: 
    print ('This program requires a number greater than 0 to function.')
    print ('This program will now terminate, restart if you wish to continue.')