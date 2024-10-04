#Program to take user input (float), divide in ratio 60:40
#Calculate tax due on diff amounts (23% on larger, 41% on smaller)
#Print out initial amount, two different tax amounts, total tax, total nett income
#Program needs to check that input is non-negative. If negative, needs to print "Amount of income must be >=0. Please try again."

gross_income=float(input('Please enter the income:'))

if gross_income < 0:
    print ('Amount of income must be >=0. Please try again.')
else: 
    tax_60=(((gross_income/10)*6)/100)*23    #tax due on 60% of lump sum
    tax_40=(((gross_income/10)*4)/100)*41    #tax due on 40% of lump sum 
    print ('Initial amount is:', gross_income)
    print ('Tax due on 60 percent of the income:', tax_60)
    print ('Tax due on 40 percent of the income:', tax_40)
    print ('Total tax due:', tax_40+tax_60)
    print ('Nett income is:', gross_income-(tax_40+tax_60))
    print ('Finished!')