#implement the program that illustrates scoping in Python from the lectures 
#from Page 12 of the notes on Lecture 15, the section on “Scoping”.
#adapt the code to include extra variables and operations, to ensure understanding

#PSEUDOCODE 
#define the function (x)
    #set function docstring to explain that the function completes a variety of computations
#print out the values that exist before calling the function 
#then call the function and print the values that result from it 
#print the values that exist after function(x), with alterations to a and b 

def f(x):
    """Function that completes a range of computations and prints out the results"""
    print('In function f:')
    x += 1
    y = 1
    a=i**2
    b=i%2
    print('x is', x)
    print('y is', y)
    print('z is', z)
    print ('a is', a)
    print ('b is', b)
    return x

x, y, z, a, b, i = 5, 10, 15, 20, 25, 30 #These details are printed first 
print('Before function f:')
print('x is', x)
print('y is', y)
print('z is', z)
print ('a is', a)
print ('b is', b)

z = f(x) #x in the function is 5+1, therefore z=6
b=a
a=i-a
print('After function f:')
print('x is', x) #both x and y return to their initial print values 
print('y is', y)
print('z is', z)
print ('a and b together are', str(a+b))