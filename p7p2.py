#Creating an algorithm to determine whether a year is a leap year, using Wikipedia algorithm
#if (year is not exactly divisible by 4) then (it is a common year)
#else
#if (year is not exactly divisible by 100) then (it is a leap year)
#else
#if (year is not exactly divisible by 400) then (it is a common year)
#else (it is a leap year)
#above from Lecture 8 slides - referenced as algorithm from Wikipedia

#pseudocode - my interpretation
#year=integer(user input(please enter a year))
#if year%4!=0, then print that it is a common year 
#else if year%100, print year is a leap year 
#else if year%400, print year is a common year 
#else print year is a leap year 
#print finished 

year=int(input('Please enter a year:'))

if year%4!=0:
    print (year, 'is a common year.')
elif year%100:
    print(year, 'is a leap year.')
elif year%400!=0:
    print (year, 'is a common year.')
else: 
    print(year, 'is a leap year.')

print('Finished!')