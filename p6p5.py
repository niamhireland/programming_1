#Define password as lovepython 
#Define attempt as user input (cue of 'Please enter your password)
#If attempt is equal to password, print 'You have successfully logged in.'
#Else if attempt is incorrect, print 'Sorry, the password is wrong'
    #Define attempt_1 as user input (Please input your password)
    #If attempt_1=password, print 'Thank you, that was correct'.
        #Repeat previous step. 
            #if password is correct on third repetition, print, you have successfully logged in. 
    #else print 'You have been denied access.' and exit 

password='lovepython'
attempt=input('Please enter your password:')

if  attempt==password:
    print ('You have successfully logged in.')
elif attempt!=password:
    print('Sorry, the password is wrong.')
    attempt_1=input('Please input your password:')
    if attempt_1==password:
        print('Thank you, that was correct.')
        attempt_2=input('Please repeat your password:')
        if attempt_2==password:
            print('Thank you, that was correct.')
            attempt_3=input('We require one final submission of password:')
            if attempt_3==password:
                print('You have successfully logged in.')
    else:
        print('You have been denied access.')
   