#Prompting user to enter a number. 
#using said number in a while loop to generate a multiplication table, ranging from 0-20

#Prompt user to enter a value of their choice 
#Limit table size to 20 (defining it as an int)
#set i to 1 

#if user enters 0 or less, highlight the error to the user and terminate the program. 

#else, print a heading for the table\
#if i is less than/equal to table size (aka 20), print i*user input
#continue this until the limit of 20 is reached, then print 'Finished!'

print ('This program generates a multiplication table, up to and including 20x.')
user_selection=int(input('Please enter the size of the table:'))
table_size=int(20)
i=0

if user_selection<=0:
    print ('This program requires a positive integer.')
    print ('Please restart the program if you wish to try again.')
else:
    print (str(user_selection), 'Times Table')
    while i<=table_size:
        print (str(i), 'times', str(user_selection), 'is', i*user_selection)
        i+=1
    print ('Finished!')
