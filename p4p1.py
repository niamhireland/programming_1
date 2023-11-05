#TASK 
#Write a program that takes as input an amount of currency (a float) and an exchange rate to another currency(a float) and prints out the value of the original amount 
#in the other currency. For the exchange rate, pick two currencies and use today’s exchange rate.

#Converting currencies, using user input as initial currency.
#This program will convert Euro to Mexican Peso.
#According to xe.com, Euro-Mexican Peso conversion rate is 18.28 on 21/9/23.

#A program prompt to ensure user understanding
print ('Welcome to the Euro-Mexican Peso converter!')
euro_nett=input('Enter the amount of Euro you wish to convert:')

#Converting the value input by the user 
#Firstly converting a given int to a float 
euro_float=float(euro_nett)

#Then restating the given values before releasing final conversion
print ('From Euro:', euro_float)
to_pesos=euro_float*18.28 #Euro amount multiplied by conversion rate
print('To Mexican Pesos:', to_pesos)
