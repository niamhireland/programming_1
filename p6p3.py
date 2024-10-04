#Ask the user for their name. 
#If the name reads as 'Niamh', print 'That is a cool name'
#If the name reads as 'Mickey Mouse' or 'Spongebob Squarepants', print 'Are you sure that is your name?'
#Else (for all other names) print 'You have a nice name'.

name=input('What is your name?')
if name=='Niamh':
    print('That is a cool name!')
    print('Finished!')
elif name=='Mickey Mouse' or name=='Spongebob Squarepants':
     print('Are you sure that is your name?')
     print('Finished!')
else:
     print('You have a nice name.')
     print('Finished!')