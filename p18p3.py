#TASK 
#Write a function that takes a string as an argument and returns the number of times that
#the string “code” (case-sensitive) appears anywhere in the given string, except that any letter
#will be accepted for the “d”, so “that cope”, “cooe” and “coDe” will also be accepted, but
#co3e”, “co-e” and “coe” will not be.

#PSEUDOCODE 

#import re

#define function (seekcode)
    #compile all instances of co_e, where _ is an alphabet character 
    #set list 'matches' to contain all instances of the pattern 
    #return the length of the matches to the function

#request user to input the word code 
    #while the input isn't Enter, call function and print function result 

import re 

def seekcode(input_str):
    pattern = re.compile (r'co[abcdefghijklmnopqrstuvwxyz]e')
    matches = pattern.findall(input_str)
    return len(matches)

input_str = input('This is a counting exercise. Enter the word \'code\' as many times as you like. Press Enter to exit: ')

while input_str != "":
    print (f'You entered \'code\' {seekcode(input_str)} times.')
    input_str = input('This is a counting exercise. Enter the word \'code\' as many times as you like. Press Enter to exit: ')

print ('Finished!')