#TASK

#Write a program that takes a page (eg the source of a Web page that you have saved), counts the occurrences of left angle 
#brackets (<), right angle brackets (>), newlines, the lowercase letter e, the string <!-- and the string --> and prints out
#the results to a file results.txt. Your program should make appropriate checks regarding the existence of the input and 
#output files.

#PSEUDOCODE 

#open the file 'farmaphobia.txt'
#read the file for each separate target and print out result 
#if file cannot be located, print same. 

filepath = 'farmaphobia_info.txt'

try: 
    with open(filepath, 'r') as fileHandle:
        file_contents = fileHandle.read
        left_angle_bracket_count = file_contents.count('<')
        print (f'The number of left angle brackets is: {left_angle_bracket_count}')
        right_angle_bracket_count = file_contents.count('>')
        print (f'The number of right angle brackets is: {right_angle_bracket_count}')
        e_count = file_contents.count('e')
        print (f'The instance of lowercase \'e\' is: {e_count}')
        newline_count = file_contents.count('\n')
        print (f'The instance of \'\\n\' is: {newline_count}')
        excl_1_count = file_contents.count('<!--')
        print (f'The instance of \'<!--\' is: {excl_1_count}')
        end_excl_count = file_contents.count('-->')
        print (f'The instance of \'-->\' is: {end_excl_count}')

except FileNotFoundError:
    print (f'The file {filepath} was not found.')