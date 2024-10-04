from math import pi 

length = float(input('Please enter a measurement:'))

if length < 0:
    print ('Length must be >0. Please try again.')
else:
#Finding the area of a square with side equivalent to user input 
#Square area = length * width
    print ('Area of a square with side equivalent to your input:', length*length)
    print ()

#Volume of a cube with side equivalent to user input 
#Cube volume = length*width*height 
    print ('Volume of a cube with side equivalent to your input:', length**3)
    print ()

#Area of a circle with radius equal to user input
#Area of a circle = pi * radius squared
    print ('Area of a circle with radius equivalent to your input:', pi*(length*length))
    print ()

#Volume of a sphere, let radius equal user input 
#Volume of a sphere = 4/3 pi radius**3
    print ('Volume of a sphere with radius equivalent to your input:', ((4/3.0)*pi)*(length**3))
    print ()

#Volume of a cylinder with radius and side equal to user input. 
#Cylinder volume = pi x cylinder radius squared x cylinder height 

    print ('Volume of a cylinder with radius and side equal to your input:', pi*(length**2)*length)