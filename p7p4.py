#Using a while loop to sum the first 5000 integers and print the total 

#Establish that initial total=1 and initial count=0
#While count<=5000:
    #total=count+total 
    #Add +1 to count, to indicate another loop cycle has passed. 
#Print total when the loop count has reached 5000

total=0 #running total
count=1 #count total

while count<=5000:
    total=count+total
    count=count+1

print('Total is:', total)