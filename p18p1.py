#TASK
#Write an iterative version of an isPal function to check whether a supplied string is a palindrome.

#PSEUDOCODE 

#define function isPalindrome
    #within the function, define isChars to convert string to lowercase and remove special letters
        #use s.lower to convert into lowercase
        #set up an empty string to contain letters 
        #iterate through string
            #if alphabet letter is found in string, add it to the letterstring
        #return the letterstring 
    #new function isPal 
        #utilising previous function's letterstring 
        #define values left and right, compare both 
            #if they are not equivalent, return False 
            #else decrement right by 1, increment left by 1 and compare letters again 

#request user input of string 

#while user input isn't Enter, call the function and evaluate whether the input is a palindrome
#else terminate program 

def isPalindrome(string):
    """overall function for evaluating whether a string is a palindrome"""
    def isChars(string):
        '''Converts string to lowercase, removes any special characters/whitespace'''
        string = string.lower()
        letterstring = ""
        for s in string: 
            if s.isalpha():
                letterstring += s
        return letterstring
    def isPal(letterstring):
        '''evaluates whether a string is a palindrome or not'''
        left, right = 0, len(letterstring) - 1
        while left < right: 
            if letterstring[left] != letterstring[right]:
                    return False
            left += 1
            right -= 1 
        return True 
    return isPal(isChars(string))

string=input('Enter a string (empty string to exit): ')

while string != "":
    if isPalindrome(string):
        print (f'{string} is a palindrome.')
    else: 
        print (f'{string} is not a palindrome.')
    string=input('Enter a string (empty string to exit): ')

print ('Finished!')