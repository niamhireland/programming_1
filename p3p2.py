#Using a single length to calculate the measurement of a range of shapes 
#Length selected = 232222.13 - my student number, as per instructions

#Calculating the area of a square 
length=232222.13 #length of the side of the square 
print ('The area of a square with side 232222.13:', length**2) 
#Squaring the length (using**) will return the area 

#Calculating the volume of a cube utilising the length of one side 
length=232222.13 #length of the side of the cube 
#To find the volume of a cube, we multiply length x breadth x height 
#As all sides of a cube are equal, we have all of these measurements already 
#Therefore, we must cube (x3) the given length
print ('The volume of a cube with side length 232222.13:', length**3)

#Finding the area of a circle from a given diameter 
diameter=232222.13 #as per instructions in practical sheet 
#area of a circle=pi multiplied by radius squared 
#radius = half the diameter 
radius=diameter/2
r=radius**2 #in order to complete the formula 'pi x radius squared'
pi=3.1415927 #as per practical sheet instructions
print ('The area of a circle with diameter 232222.13:', pi*r)

#Calculating the volume of a sphere from a given diameter 
diameter=232222.13 #as per instructions in practical sheet 
#volume of a sphere is 4/3 pi r**3, where r=radius 
radius=diameter/2 #in order to give the radius for the equation
pi=3.1415927 #as per practical sheet instructions 
sphere_volume=((4/3.0)*pi)*radius**3
print ('Volume of a sphere with diameter of 232222.13:', sphere_volume)

#Calculating the volume of a cylinder from a given diameter and side length 
#Cylinder volume = pi x cylinder radius squared x cylinder height 
cylinder_height=232222.13 #Let side length = cylinder height 
diameter=232222.13 #As per instructions in practical sheet 
radius=diameter/2 #As radius is required for this equation
pi=3.1415927 #As per practical sheet instructions 
cylinder_volume=pi*(radius**2)*cylinder_height
print ('Volume of a cylinder with diameter&side 232222.13:', cylinder_volume)
