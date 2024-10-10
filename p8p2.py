#prompt the user for a number and use a while loop to generate a multiplication table, from 1 up to and including that number 

#Get user to input a positive integer 
#If negative number is input, inform the user of same and terminate the program. 
#Else:
    #Set i as equal to 1 
    #While i is less than the user number+1:
        #set j as equal to 1
            #while j is less than or equal to the user's number:
            #print i * j, followed by a blank space 
            #increment j by 1 
            #repeat until j is equal to table size 
        #print a newline 
        #increment i by 1 
            #loop resumes 

print ('This program takes a positive integer and generates a multiplication table from it.')
print ('The multiplication table begins from 1 and continues to the given number (including said number.)')
table_size = int(input('Enter your selected number:'))

if table_size<=0:
    print ('This program requires a number that is greater than 0.')
    print ('Restart the program if you wish to try again.')

else:
    i = 1
    while i < table_size+1: #incrementing table size by 1, in case user inputs 1
        j = 1
        while j<=table_size:
            print(i * j, " ", end = "")
            j += 1
        print()
        i += 1