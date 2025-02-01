# implement a program that uses a function max 
#program is from slide 5 of lecture 15 notes, as per instructions 

#PSEUDOCODE 
#define the max function to include (a,b)
#include a docstring that states the function returns the largest of the arguments 
#if a is greater than b, return a 
# otherwise return b 

#request user to input two numbers 
#print the two numbers and which of the numbers is larger, then print 'Finished!'


def max(a, b):
    """Function that returns the largest of its two arguments"""
    if a > b:
        return a
    else:
        return b

number1 = float(input('Enter a number: '))
number2 = float(input('Enter a number: '))
print('The largest of', number1, 'and', number2, 'is', max(number1, number2))

print('Finished!')