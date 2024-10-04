#Program taking currency input and prints value of original amount in another currency 
#Input must be float or converted to float
#Exchange rate must be float 
#Program must check that user input is non-negative 
#If amount is negative, must print "Amount must be >= 0. Please try again" before exiting.

#1Euro=18.4737 Mexican pesos on 26/9/23, as per xe.com
peso_conversion_rate=18.4737
print ('Welcome to the Euro-Mexican Peso converter!') #ensure user understanding
euro_amount=float(input('Enter the amount of Euro you wish to convert:'))
print ('Amount in Euro:', euro_amount)

if euro_amount < 0:
    print ('Amount must be >= 0. Please try again.')
else:
    print ('Amount in Mexican Pesos:', euro_amount*peso_conversion_rate)
    print ('Finished.')
