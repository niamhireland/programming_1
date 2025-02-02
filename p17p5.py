#TASK 
#Implement a variation of the palindrome program that prints out messages to allow you to trace how it works.

#PSEUDOCODE 
#Please note: implemented print statement is on line 63.
#Info: This code is from Lecture 17, slide 18 - 21 as per instructions 

#define the function IsPalindrome 
    #define function toChars
        #set s to equal lowercase and an empty string
        #iterate through s 
            #if each character in the string can be found in the alphabet (lowercase):
                #add it to the letterstring
                #therefore all non-letters will not be included 
    #define function IsPal
        #if s is less than/equal to 1: 
            #print a statement of what the string currently is and that the first and last letters match 
            #return True (as a string of 1 letter is defined as a palindrome)
        #else 
            #compare first and last letters of s [0] and [-1] and then compare the remainder of the string
            #return that it is a palindrome (if it is)

#get user to input a string 

#while the string is not empty: 
    #if it is a palindrome (according to the function), print message of same 
    #if it is not a palindrome, print according message 
    #ask for repeat input from user 
#if user enter an empty string, the while loop terminates and 'Finished!' is printed. 

# Program to check whether a string is a palindromes
# Prompts the user for strings and checks each one
# Exits when an empty string is entered
def isPalindrome(s):
    """Checks whether the string s is a palindrome
Assumes s is a str.
Returns True if the letters in s form a palindrome;
Returns False otherwise.
Case and non-letters are ignored."""

    def toChars(s):
        """Converts a string to lowercase and removes non-letters
Assumes s is a str.
Converts uppercase letters to lowercase and removes non-letters."""
# First of all, convert uppercase letters to lowercase
        s = s.lower()
# Start with an empty string
        letterstring = ''
# Go through s...
        for c in s:
# ... and add the character to the string if it is a letter

            if c in 'abcdefghijklmnopqrstuvwxyz':
                letterstring += c
        return letterstring
    
    def isPal(s):
        """Checks whether the string s is a palindrome
Assumes that s is a str with only lowercase letters and no
non-letters.
Returns True if s is a palindrome;
Returns False otherwise.
Recursive function."""
        if len(s) <= 1:
            print (f'String is currently {s}. First and last characters match.') #Here is my implemented print statement to see the calculation of the palindrome
# A palindrome of length 0 or 1 is a palindrome
            return True
        else:
# Compare the first and the last letters and check the remainder
# of the string
            return s[0] == s[-1] and isPal(s[1:-1])
    return isPal(toChars(s))

str = input('Enter a string (empty string to exit): ')
while str != '':
    if isPalindrome(str):
        print(str, 'is a palindrome')
    else:
        print(str, 'is not a palindrome')
    str = input('Enter a string (empty string to exit): ')
print('Finished!')