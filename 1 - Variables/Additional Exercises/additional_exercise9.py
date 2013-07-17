#16-01-2012
#additional exercise 9
#sample solution

import math

print("Circular Swimming Pool")
print("This program calculates the volume of a circular swimming pool")
print()
diameter = float(input("Please enter the diameter of the pool: "))
depth = float(input("Please enter the depth of the pool: "))
radius = diameter/2
#radius**2 means radius squared
area = round(math.pi * radius**2,2)
volume = round(area * depth,2)
print()
print("The volume of the swimming pool is {0}.".format(volume))

