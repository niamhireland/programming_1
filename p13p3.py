# Program to print out the largest of two numbers entered by the user
# Uses two functions: max and print_max

#PSEUDOCODE 
#define the print_max function and include a docstring explaining that the function identifies which of two numbers is largest
#request user to input two numbers (convert these to floats)
#call the function and print out the resulting values 


def print_max():
    """Function that prints out the largest of two numbers, Uses the function max to find the largest"""
    def max(a, b):
        '''Function that returns the largest of its two arguments'''
    if a>b:
        return a
    else:
        return b

number1 = float(input('Enter a number: '))
number2 = float(input('Enter a number: '))
print('The largest of', number1, 'and', number2, 'is', max(number1, number2))