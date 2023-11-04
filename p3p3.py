#TASK
#Write a program that takes an amount (a float), divides the amount in the ratio 60:40, calculates the tax due according to two different tax rates 
#(13.5% on the larger amount and 23% on the smaller) and prints out the total amount (initial amount plus taxes).

#Calculating tax due 
nett=232222.13 #float derived from student number as per instructions
print ('Initial sum:', nett)

#Splitting the nett into a 60:40 ratio 
ratio_section_60=(nett/10)*6 #Which will give six tenths of starting sum
ratio_section_40=(nett/10)*4 #which will give four tenths of starting sum

#Calculating tax rate 13.5% on larger amount (60%)
lower_tax_rate=13.5/100 
lower_tax_due=lower_tax_rate*ratio_section_60

#Calculating tax rate 23% on smaller amount (40%)
higher_tax_rate=23/100 
higher_tax_due=higher_tax_rate*ratio_section_40

#Adding both tax bands together 
total_tax_due=higher_tax_due+lower_tax_due

print ('Total tax due:', total_tax_due) #Showing owable tax

print ('Total amount:', nett+total_tax_due ) #Total amount including tax
