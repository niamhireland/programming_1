#TASK 
#Write a function that takes a string as an argument and returns the number of times that the
#string “code” (case-sensitive) appears anywhere in the given string.

#PSEUDOCODE 

#define function (seekcode)
    #if 'code' can't be found in the string, return False 
    #else use count to count how many times code appears in the string 
    #return count value 

#request user to input the word code 
    #while the input isn't Enter, call function and print count result 

def seekcode(input_str):
    count = 0
    if 'code' not in input_str:
        return False 
    else:
        count = input_str.count('code')
    return count

input_str = input('This is a counting exercise. Enter the word \'code\' as many times as you like. Press Enter to exit: ')

while input_str != "":
    print (f'You entered \'code\' {seekcode(input_str)} times.')
    input_str = input('This is a counting exercise. Enter the word \'code\' as many times as you like. Press Enter to exit: ')

print ('Finished!')