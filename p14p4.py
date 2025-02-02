#Using the program developed in Question 3 as a starting point write a program that searches for 
#prime numbers in a range of integers. Program should print out an appropriate message if a number is a prime number. 
#This program should print out all the pairs of factors for a non-prime number. 

#PSEUDOCODE 
#for number in the range (2, 20): 
#give is_prime the Boolean value true 
#create an empty list for factors 

#for i in range (2, number)
    #if the number can be evenly divided by i:
        #append the factors list with (i, number (floor) divided by i)
        #is_prime is False 

    #if not is_prime (aka is composite)
    #for each factor in the factors, print the number equals factor 0 x factor 1 
    
    #else (the number is prime)
        #print a message stating same 

for number in range(2, 20):
    is_prime = True
    factors = []

    for i in range(2, number):
        if number % i == 0:
            factors.append((i, number // i))
            is_prime = False

    if not is_prime:
        for factor in factors:
            print(number, 'equals', factor[0], '*', factor[1])
    else:
        print(number, 'is a prime number')