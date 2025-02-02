# Program to illustrate the use of the else statement on a for loop
# Search for prime numbers in a range of integers
# Look for prime numbers in a range of integers
#program taken from slide 16 of lecture 13, as per task instructions 

#PSEUDOCODE 
#for a number in range 2-20: 
    #steadily increment i 
    #for i in range 2-20
        #if number divided by 1=0: (therefore is a composite number)
            #print that the number equals i times the number divided by i 
    #else (so the number is prime)
        #print a message to the same effect 

for number in range(2, 20):
    for i in range(2, number):
        if number % i == 0:
            print(number, 'equals', i, '*', number//i)
            break
    
    else:
        # loop fell through without finding a factor
        print(number, 'is a prime number')
print('Finished!')