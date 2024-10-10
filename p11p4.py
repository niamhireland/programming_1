#have user enter a number 

#define a Catalan number calculation
    #if number is less than 0, return 0
    #if number is 0, return 1 
    #calculate the range of the number+1, starting on 1 and incrementing by 1 
        #complete Catalan formula for each incrementing number, as per task sheet formula

#ask the user to input an int
#if user enters a number less than 0, print message that Catalan numbers are not defined for this and the program will terminate.
#else, print out the resulting Catalan number from the definition

def calculate_catalan(number):
    if number<0:
        return 0 #Because Catalan numbers are non-negative numbers
    if number==0:
        return 1
    catalan_number=1
    for i in range (1, number+1, 1):
        catalan_number=catalan_number*(4*i-2)
        catalan_number=catalan_number//(i+1)
    return catalan_number

print ('This program takes a given number and returns the Catalan number of it. Negative numbers will cause the program to terminate.')
number=int(input('Enter a number:'))

if number<0:
    print ('Catalan numbers are not defined for non-negative numbers.')
    print ('Please restart the program if you wish to try again.')
else:
    result=calculate_catalan(number)
    print ('The number you entered is', number, '.')
    print ('The Catalan number of this number is', calculate_catalan(number))
