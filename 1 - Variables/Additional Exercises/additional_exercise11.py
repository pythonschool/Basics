#16-01-2012
#additional exercise 11
#sample solution

import math

print("Ladder Height")
print("This program calculates how far a ladder reaches up a wall")
print("when given the number of degrees the ladder makes with the horizontal")
print("and its distance from the wall.")
print()
degreesFromHorizontal = float(68)
distanceFromWall = float(1.5)
#degrees in radians
radiansFromHorizontal = math.radians(degreesFromHorizontal)
#tan
tan = math.tan(radiansFromHorizontal)
wallReach = round(tan * distanceFromWall,2)
print("The ladder reaches {0} up the wall.".format(wallReach))


    
