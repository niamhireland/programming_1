#Num1=request user input of an int 
#Num2=request user input of an int 
#Num3=request user input of an int 

#if num1 is greater than num2 and num3:
    #if num1 can not be evenly divided by 2:
        #print "num1 is the largest number and is an odd number."
#if num2 is greater than num1 and num3:
    #if num2 can not be evenly divided by 2:
        #print "num2 is the largest number and is an odd number."
#if num3 is greater than num2 and num1:
    #if num3 can not be evenly divided by 2:
        #print "num3 is the largest number and is an odd number."
#else if none of the above applies:
    #print "None of these are odd numbers."

num1=int(input('Please enter a number:'))
num2=int(input('Please enter another number:'))
num3=int(input('Please enter one more number:'))

if num1>num2 and num1>num3:
    if num1%2!=0:
        print(num1, "is the largest number and is an odd number.")
elif num2>num1 and num2>num3:
    if num2%2!=0:
        print(num2, "is the largest number and is an odd number.")
elif num3>num2 and num3>num1:
    if num3%2!=0:
        print(num3, "is the largest number and is an odd number.")
else: 
    print('None of these are odd numbers.')