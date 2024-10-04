#Write a program that sums the integers in the range 1–10 000 that are divisble by 3 or by 5 and prints out the total

#While count (of loops) is less than or equal to 10,000:
    #Let sum = current count +0
    #if sum is divisible by 3, add it to div_3
    #if sum is divisible by 5, add it to div_5
    #add 1 to current count
    #add sums in div_3 and div_5
    #print result with 'Total is" before sum result

count=1 #count of numbers 
div_3=0
div_5=0

while count<=10000:
    sum=count+0
    if sum%3==0:
        div_3=sum+div_3
    elif sum%5==0:
        div_5=sum+div_5
    count=count+1
    total_sum=div_3+div_5

print('Total is:', total_sum)