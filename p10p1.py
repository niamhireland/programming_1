#prompt the user for an integer 
#go through the integers (start at 0), using exhaustive enumeration checking whether the square of the integer is equal to the number entered.
#if the program isn't a perfect square, print out an answer to that effect
#program should exit when a negative number is entered 

#PSEUDOCODE
#Take a user input of an integer (ensure that it is float)
#Set epsilon to 0.01, step to epsilon**2, initial root to 0.0 and initial number of guesses to 0

#if the number is less than 0, the program prints that it requires a positive integer to function.
#while the number-root**2 is greater than/equal to epsilon and root is less/equal than number:
    #increment root by step 
    #increment number of guesses by 1 
#print the total number of guesses 
#if the number-root**2 is greater than epsilon, print the resulting square root of the number
    #if the root can be evenly divided by 1, it is a perfect square - print message to this effect.
    #if the root can not be evenly divided by 1, it is not a perfect square - print message to this effect.
#else if an answer cannot be found, program prints sentence to that effect.

print ('This program takes a given int and finds the integer square root of it.')
number=float(input('Please enter a positive integer:')) #gaining input from user 

epsilon=0.01
step=epsilon**2
root=0.0
numGuesses=0

if number<0:
    print('This program requires a positive integer to function.')

while abs(number-root**2)>=epsilon and root<=number:
    root+=step
    numGuesses+=1
print ('Number of guesses:', numGuesses)
if abs(number-root**2)<epsilon:
    print ('The approximate square root of', number, 'is', root)
    if root%1==0:
        print ('This is a perfect square.')
    if root%1!=0:
        print ('This is not a perfect square.')
else:
    print ('Failed to find a square root of', number)