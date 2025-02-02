#TASK
#Write a Python program that checks whether the strings “cat” and “dog” appear the same number of times
#in a given string input by the user.

#PSEUDOCODE 

#create function meowbark 
    #set initial count of total cats and total dogs to 0, respectively 
    #if cat appears in the animals string, add each instance to the count of 'cat' in animals 
    #if dog appears in the animals string, add each instance to the count of 'dog' in animals 
    #if total dogs is greater than total cats:
        #create variable 'how_many more' to hold the value of dog-cat
        #print how many times dog and cat were entered and the difference between them 
    #if total cats is greater than total dogs: 
        #repeat the above (swapping the order of total_dogs and total_cats for the subtraction)
    #if total_cats and total_dogs are equal, print out statement of same

#get the user to type the words 'cat' and 'dog' as many times as they like 

#if 'cat' or 'dog' is contained in the string: 
    #call the function meowbark 
#else print an error message 

def meowbark(animals):
    """A function to evaluate whether the words 'cat' or 'dog' appear in a string. 
Function assumes only cat and dog are contained in the string.
Function compares whether instance of 'cat' or 'dog' is higher and prints out result."""
    total_cats=0
    total_dogs=0
    if 'cat' in animals: 
        total_cats=animals.count('cat')
        #print (f'Total times you typed cat: {total_cats}')
    if 'dog' in animals: 
        total_dogs=animals.count('dog')
        #print (f'Total times you typed dog: {total_dogs}')
    if total_dogs>total_cats:
        print (f'You typed "dog" {total_dogs} times and "cat" {total_cats} times.')
        how_many_more=total_dogs-total_cats
        print (f'That means you typed "dog" {how_many_more} more time(s) than you typed "cat".')
    if total_cats>total_dogs:
        print (f'You typed "dog" {total_dogs} times and "cat" {total_cats} times.')
        how_many_more=total_cats-total_dogs
        print (f'That means you typed "cat" {how_many_more} more time(s) than you typed "dog".')
    if total_cats==total_dogs:
        print (f'You typed "dog" {total_dogs} times and "cat" {total_cats} times.')
        print ('That means you love us both equally!')

animals=input('Type the words "cat" and "dog" as many times as you like:')

if 'cat' in animals or 'dog' in animals:
    meowbark(animals)
else: 
    print('You didn\'t type cat or dog, so this function can\'t execute.')
