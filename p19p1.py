#TASK
#Write a Python function that takes a number in base 10 and a base, both positive ints, and,
#using the algorithm presented in lectures, returns the number in the base supplied.

#PSEUDOCODE 
#within the function: 
    #while the base 10 number is larger than 0:
        #divide it by the second input number (the base the user wishes to convert it to)
            #append the remainder of that division to a list 
            #floor division to find the new number to divide by 
                #let decimalnum = floor division result and continue the loop 
        #in order to turn it into a base number: 
            #reverse the element order in the list 
            #convert the elements into strings 
            #join the elements together with no spaces between 
    #return result 
#outside of the function, if user input is greater than 0:
    #call and print function 

def baseconverter(decimalnum):
    """Function to change a number from base 10 to another base
Function assumes that number inputs are positive ints
Function divides number by another given number, retains remainders as a list and returns list as result"""
    remainders=[]
    while decimalnum > 0:
        remaindernum = decimalnum % newbase
        remainders.append(remaindernum)
        decimalnum = decimalnum // newbase
    result = "".join(map(str, remainders[::-1]))
    return result


decimalnum = int(input('Enter a number in base 10:'))
newbase = int(input('What base do you wish to convert it to?'))

if decimalnum>0:
    print (f'The decimal number you input is {decimalnum}. The base you wish to convert into is: {newbase}.')
    print (f'When converted, the number is: {baseconverter(decimalnum)}.')
else:
    print('Number input must be greater than 0.')