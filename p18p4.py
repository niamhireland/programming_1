#TASK

#Write a function that takes as arguments two strings and returns True if either of the strings appears at the very end of 
#the other string, ignoring upper/lower case differences (in other words, the computation should not be case sensitive). 
#Recall that s.lower() returns the lowercase version of a string.

#PSEUDOCODE
#request user input of two strings 
#define function 
    #convert both strings to lowercase 
    #return if one of the strings ends with the other one 

def do_they_match(string1, string2):
    firststring = string1.lower()
    secondstring = string2.lower()
    return firststring.endswith(secondstring) or secondstring.endswith(firststring)

string1 = input('Enter a string: ')
string2 = input ('Now enter another string: ')

if do_they_match(string1, string2): 
    print('True. One of these strings is at the end of the other string.')
else: 
    print('False. Neither of these strings are at the end of the other string.')