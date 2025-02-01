#implement programs that demonstrate the definition and use of functions in Python from lectures 
#incorporate docstrings to document the functions 
#the function below is from slide 4 of lecture 15 notes, as per instructions

# Program to print out the largest of two numbers entered by the user

#PSEUDOCODE
#define the max function of a and b:
    #if a is greater than b, return a 
    #otherwise return b 
#request user to input two numbers 
#use 'biggest' variable to hold the max function 
#print out the largest number

def max(a, b):
    """Function that returns the largest of its two arguments"""
    if a > b:
        return a
    else:
        return b
 
number1 = float(input('Enter a number: '))
number2 = float(input('Enter a number: '))
biggest = max(number1, number2)
print('The largest of', number1, 'and', number2, 'is', biggest)
print('Finished!')