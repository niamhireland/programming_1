# Finding the integer cube root of a number

#firstly, prompt the user for a number 
#set cube root to equal 0 
#set a while loop to establish the cube root 

# for cube root in the range (absolute number plus 1)
    #if cube root**3 is greater than/equal to the absolute number
        #break
    #if cube root**3 is equal to absolute number
        #if number is less than 0 
            #cube root is the same as minus cube root 
    #print the cube root 
#for anything else, print ('Cube root is not a perfect cube')
#print 'Finished!'

number = int(input('Enter the number for which you wish to calculate the cube root: '))

cube_root = 0
while cube_root ** 3 < abs(number):
    cube_root += 1

for cube_root in range(abs(number) + 1):
    if cube_root ** 3 >= abs(number):
        break
    if cube_root ** 3 == abs(number):
        if number < 0:
            cube_root = -cube_root
    print('Cube root of', number, 'is', cube_root)

else:
    print(number, 'is not a perfect cube.')
    print('Finished!')