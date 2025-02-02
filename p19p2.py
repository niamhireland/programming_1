#TASK

#Write a function that takes a string of digits, representing a number, and a base (an int) as
#arguments, and returns the number in decimal (Base 10). The digits should include the letters
#A–F (uppercase and lowercase), so that hexadecimal numbers can be supplied and converted.

#PSEUDOCODE 
#create function to convert other values to decimal 
    #map the hexadecimal values to their decimal counterparts
    #set a result variable to track the decimal result 
    #convert characters in user's input to lowercase 
    #iterate through the string, starting at the end 
        #if the character is found in the hexa_values list, rename it to variable 'digit'
        #else it's a digit, so just convert it to an integer 
    #increment the result variable by the digit (times base)

#request user to input a value and a base 
#call function and print result 

def decimalversion(to_convert):
    """Function to convert values into decimal from another base system.
Function assumes that positive values will be entered."""
    hexa_values = {'a':10, 'b':11, 'c':12, 'd':13, 'e':14, 'f':15}
    result = 0
    to_convert = to_convert.lower()
    for char in to_convert[::-1]:
        if char in hexa_values:
            digit = hexa_values[char]
        else: 
            digit = int(char)
        result += digit * base 
    return result 

to_convert = input('Enter a number in a base from 1-16 (excluding 10):')
base = int(input('What base is your previous number in?'))

print (f'You entered the value {to_convert} and stated this is in base {base}.')
print (f'In decimal, the value you entered is {decimalversion(to_convert)}.')