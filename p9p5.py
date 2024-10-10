#Have user enter values for number of toppings in total and number of toppings allowed per user 
#Calculate the factorial for both values separately 
#If difference=0, return 1 (as there is one pizza available with no variation)

#PSEUDOCODE
#Get user to input the total toppings and toppings allowed as separate, positive integers.
#If user enters negative numbers, terminate the program and inform them of same. 
#If total toppings and/or toppings allowed = zero, there is only one option available. 
    #print out the above for the user 

#Calculate the factorial for toppings allowed and total toppings: 
    #if 1 is entered for either, set factorial to be 1 
    #while i is less than/equal to the user input number:
        #multiply the current factorial count by i 
        #increment i 

#Find the difference between the two original numbers
    #if difference =0, return 1 (because there is no pizza choice available)

#else: 
    #follow all formula steps (in separate tasks to aid comprehension)
    #print result for user 


toppings_total=int(input('How many toppings in total are available today?')) #Prompt user for available toppings
toppings_allowed=int(input('How many toppings can each customer avail of today?')) #Prompt user for how many toppings customers may have

if toppings_total<0 or toppings_allowed<0: #if user enters negative numbers, program terminates 
    print ('Number of toppings can\'t be a negative number. Please restart the program if you wish to try again.')

if toppings_total==0 or toppings_allowed==0: #If users have no choice, there is only a plain pizza on offer that day 
    print ('Your customers have only one option - a plain pizza.')

if toppings_total>0: 
    if toppings_total==1: 
        fact_total=1 #Set 1! to be 1 
    elif toppings_total>1:
        fact_total=1
        i=1
        while i<=toppings_total:
            fact_total*=i #calculate the factorial for toppings_total
            i+=1

if toppings_allowed>0: 
    if toppings_allowed==1: 
        fact_allowed=1 #Set 1! to be 1 
    elif toppings_allowed>1:
        fact_allowed=1
        i=1
        while i<=toppings_allowed:
            fact_allowed*=i #calculate the factorial for toppings_allowed
            i+=1

difference_is=toppings_total-toppings_allowed #calculate the difference between the two
if difference_is==1:
    print ('There is only one pizza combo available to your customers today.')

else: 
    formula_step_1=(int(toppings_total)-int(toppings_allowed)) #subtract k from n
    i=1
    fact_formula=1
    while i<=formula_step_1:
        fact_formula*=i #calculate the factorial for the subtraction in previous step (k from n)
        i+=1
    formula_step_2=int(fact_allowed)*int(fact_formula) #multiply k! by (n-k)!
    formula_step_3=int(fact_total)//int(formula_step_2) #divide n! by the result of k!(n-k)!
    print('The total amount of combos you are offering today is:', str(formula_step_3))