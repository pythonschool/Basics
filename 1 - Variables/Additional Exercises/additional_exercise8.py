#16-01-2012
#additional exercise 8
#sample solution

import math

print("Circles")
print("This program asks the radius of a circle and")
print("calculates the circumference and area")

print()
radius = float(input("Please enter the radius of the circle: "))
circumference = round(2 * math.pi * radius,2)
#radius**2 means radius squared
area = round(math.pi * radius**2,2)
print()
print("The circumference of this circle is {0}.".format(circumference))
print("The area of this circle is {0}.".format(area))

