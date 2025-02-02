#TASK

#Write a program that reads a file and checks that brackets (ie ( and ), < and >, { and }
#and [ and ]) are balanced, ie there should never be a situation where there are more right
#brackets of a particular type than there are corresponding left brackets and the total number
#of right brackets should equal the number of left brackets (You do not need to consider the
#interleaving of different bracket types). Your program should return the total number of each
#bracket and a message indicating whether or not the file has balanced brackets.

#PSEUDOCODE 

#in the function, initialise a list of all brackets 
#iterate through the file character by character 
    #if a bracket in the list is found, add it to the bracket count in the list
#if the bracket count of each type is equal, return value balanced

#open the file 
#call and print function result 
#print whether brackets are balanced or not 

def check_brackets(file):
    """Function to check the bracket count in a file and evaluate if the brackets are balanced or not """
    bracket_map = {
        '(': 0,
        ')': 0,
        '>': 0,
        '<': 0,
        '{': 0,
        '}': 0
    }

    with open(file, 'r') as file: 
        for line in file: 
            for char in line:
                if char in bracket_map:
                    bracket_map[char] += 1

    balanced = all(bracket_map[open_bracket] == bracket_map[close_bracket]
                   for open_bracket, close_bracket in [('[', ']'), ('{', '}'), ('(', ')'), ('<', '>')])

    return bracket_map, balanced

file = "file.txt" 

bracket_counts, is_balanced = check_brackets(file)

print("Bracket Counts:")
for bracket, count in bracket_counts.items():
    print(f"{bracket}: {count}")

if is_balanced:
    print("The brackets in the file are balanced.")
else:
    print("The brackets in the file are not balanced.")