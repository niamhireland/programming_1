#Prompt the user for two numbers (in two consecutive requests).
#Read the numbers. 
#Find the sum of the numbers, naming it 'total'.
#if number <= 100 then print('That is a big number!')
    #else print the sum of the two numbers.
#Program finishes 

num1=(int(input('Please input a number:')))
num2=(int(input('Please input another number:')))
total=num1+num2
if total<=100:
    print('That is a big number!')
else: print('You entered ', num1, 'and ', num2, '. They sum to ', total, '.')
print('Finished!')