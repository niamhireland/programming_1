#Taking user input and calculating tax rates, along with final sum due 
#Input sum to be divided in ratio 60:40
#Tax due on larger sum: 13.5 
#Tax due on smaller sum: 23

print ('Welcome to the tax converter.')
initial_sum=input('Enter the lump sum:')

#Ensuring that the user input will be a float. 
float_amount=float(initial_sum)

#Calculating tax due at 13.5%. 
#This is due on 60% of initial sum. 
tax_60=((float_amount/10)*6)
lower_tax_payable=tax_60/13.5

#Calculating tax due at 23%
#This is due on 40% of initial sum. 
tax_40=((float_amount/10)*4)
higher_tax_payable=tax_40/23

print ('Initial amount:', float_amount)
print ('Tax due at 13.5 rate:', lower_tax_payable)
print ('Tax due at 23 rate:', higher_tax_payable)
print ('Total tax due:', higher_tax_payable+lower_tax_payable)
print ('Total amount due:', higher_tax_payable+lower_tax_payable+float_amount)
