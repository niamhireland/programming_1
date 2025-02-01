#write a function that takes as its two arguments a number and a tolerance 
#use technique from lectures to return approximation of the square root 

#PSEUDOCODE
#define the function as square root of (x)number 
#set epsilon to 0.01, root to 0.0 and step increments to epsilon squared 
#while abs(user number - root squared) is less than/equal to epsilon and root is greater than/equal to user's number: 
    #increment root by step 
    #if abs(user input - root**2)<is greater than epsilon: 
        #result = root 
    #return the result 

def sqr_root(x):
    epsilon=0.01
    step=epsilon**2
    root=0.0
    while abs(x-root**2)>=epsilon and root<=x:
        root+=step
        if abs(x-root**2)<epsilon:
            result=root
    return result

#b) Write a program that prompts the user to enter a float number. 
#If number is negative, print out error message to that effect. 
#otherwise, call the function defined in part a and print out the resulting square root

#PSEUDOCODE 
#request input of a float from the user

#if user's number is less than 0:
    #print that the program requires a positive number 
    #print that the program will terminate 
#else print the square root that results when the function is called. 

x=float(input('Enter a positive, floating-point number:'))

if x<0:
    print ('This program requires a positive number to execute.')
    print ('Restart if you wish to try again.')
else:
    print('You entered:', x, '. The approximate square root of it is:', sqr_root(x))

print ('Finished!')