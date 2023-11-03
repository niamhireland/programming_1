#TASK
#Write a program that takes an amount of currency (a float) and an exchange rate to another currency (a float) and prints out the value of the original amount in the 
#other currency. (Use today’s exchange rate for two currencies of your choice.)

#PSEUDOCODE
#Establish amount of pesos per Euro, set euro amount to be converted and print conversion.

euro_peso_conversion=18.28
                    #Number of Mexican pesos per Euro 
                    #data taken from xe.com, 21/9/23

euro_amount=232222.13
                    #Taken from student number 23222213 as per instructions

print ('Conversion rate from Euro to Mexican pesos:', euro_peso_conversion)

print ('Amount in Euro:', euro_amount)

print ('Amount in Mexican Pesos:', euro_amount*euro_peso_conversion)
