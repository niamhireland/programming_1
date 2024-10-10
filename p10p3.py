#take user input to equal word
#define vowels as a, e, i, o, u (both lower and uppercase)
#set counter and x to 0 (independently of one another) 

#if word does not equal Enter:
    #for x in word
        #if a defined vowel is present at the point of x:
            #increase count by 1
            #continue to iterate through the string
        #else (if the letter is undefined and therefore a consonant)
            #add 0 to count 
            #break
    #print the count of vowels in the word 

#if word equals Enter (blank space):
    #program terminates, print message to that effect

word=input('Enter a string. Press "Enter to exit: ')
a='a'
A='A'
e='e'
E='E'
i='i'
I='I'
o='o'
O='O'
u='u'
U='U'
count=0
x=0

if word!="":
    for x in word:
        if x==a or x==A or x==e or x==E or x==i or x==I or x==o or x==O or x==u or x==U:
            count+=1
        else:
            count+=0
            pass
    print ('There are ', count, 'vowels in this word.')

if word=="":
    print ('You pressed "Enter" and terminated this program.')
    print ('Restart if you wish to continue.')