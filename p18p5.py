#TASK

#Write a function that takes a string as an argument and returns True if the given string contains an appearance of “xyz” 
#where the “xyz” is not directly preceeded by a period (“.”).So “xxyz”, “xxyz.x.xyzz” and “xyz.xyz” are accepted but “x.xyz” is not.

#PSEUDOCODE
#request user input of a string
#define function 
    #convert string to lowercase
    #find instances of 'xyz' in the string, labelled 'index'
        #if the instance of 'xyz' is at the start of the string or not proceeded by a fullstop, returns True 
    #else returns false 

#function is called and result is stored in 'result' variable 
#print result of function using if/else

def xyz_pattern(string):
    lc_string = string.lower()
    index = lc_string.find("xyz")
    while index != -1:
        if index ==0 or lc_string[index - 1] != ".":
            return True 
        index = lc_string.find('xyz', index + 1)
    return False

string = input('Enter a string: ')
result = xyz_pattern(string)

if result is True: 
    print ('In your string, xyz was not directly preceded by a full stop.')
else:
    print ('In your string, there was an instance of \'.xyz\'. ')