#Program checks whether the name of a town or city is known to it 
#If known, program will print "You entered ___, ___ is in ___" (first/second spaces being town names and third being province)
#If not known, "Sorry, I didn't recognise that name" should print out 

ulster='Belfast', 'Derry', 'Lisburn'
connacht='Sligo', 'Galway'
leinster='Dublin', 'Kilkenny'
munster='Cork', 'Limerick', 'Waterford'

town=input('Please enter the name of a town:')

if town==ulster:
    print ('You entered', input, ',', input, 'is in Ulster.')
elif town==leinster:
    print ('You entered', input, ',', input, 'is in Leinster.')
elif town==connacht:
    print ('You entered', input, ',', input, 'is in Connacht.')
elif town==munster:
    print ('You entered', input, ',', input, 'is in Munster.')
else:
    print ('Sorry, I do not recognise that name.')