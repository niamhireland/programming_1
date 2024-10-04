#Firstly, establish a password
#Establish that the basic count is 1 (first attempt for password)
#Check that the count has not exceeded the limit
    #Ask for user input of password.
    #If password is correct, print 'You have been successfully logged in'.
    #Else if password is incorrect, print 'That was incorrect, please try again'.
        #If password count does not exceed limit, add 1 to the count and the loop will recommence. 
        #If count has been exceeded, print 'You have been denied access'.

password='lovepython'
limit=4
count=1

while count<limit:
        attempt=input('Please enter your password:')
        if  attempt==password:
            print ('You have successfully logged in.')
        elif attempt!=password:
            print('That was incorrect, please try again.')
            count+=1
            if count>=limit:
                print('You have been denied access.')