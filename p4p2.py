#TASK
#Write a program that takes as input a single length (a float) and calculates the following:
#• The area of a square with side of that length
#• The volume of a cube with side of that length
#• The area of a circule with radius of that length
#• The volume of a sphere with radius of that length
#• The volume of a cylinder with radius of that length and side of that length

from math import pi 

#Getting user input of a measurement to use in multiple conversions 
print ('This program will utilise one measurement for multiple shape measurements.')
side=input('Enter the measurement of your choice:')
float_side=float(side)
area=float_side*float_side #Squaring a square will return the area 
print ('We will first find the area of a square from the given measurement.')
print ('Area of the square:', area) 
print ('\n')


#Finding the volume of a cube from user input of one side length
#The volume of a cube is length x breadth x height 
print ('We will now calculate the volume of a cube, using the given measurement as a side length.')
volume_cube=float_side*float_side*float_side 
#As height/breadth/width are equal on a cube
print ('Volume of the cube:', volume_cube)
print ('\n')

#Finding the area of a circle with radius equal to user input.
#Area of a circle = pi x radius squared 
print ('We will now calculate the area of a circle with radius equal to the inputted value.')
print ('Area of the circle is:', pi*(float_side**2))
print ('\n')

#Finding the volume of a sphere with radius equal to user input.
#Volume of a sphere = 4/3 pi r**3, where r=radius 
print ('We will now find the volume of a sphere, let radius equal the input value.')
sphere_volume=((4/3.0)*pi)*(float_side**3)
print ('Volume of the sphere is:', sphere_volume)
print ('\n')

#Volume of a cylinder with radius and side equal to user input. 
#Cylinder volume = pi x cylinder radius squared x cylinder height 
print ('We will now find the volume of a cylinder, let the side and radius equal the user input.')
cylinder_volume=pi*(float_side**2)*float_side
print ('Volume of the cylinder:', cylinder_volume)
