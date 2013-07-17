#16-01-2012
#additional exercise 11
#sample solution

import math

print("Plane Distance")
print("This program calculates how far north and east a plane has travelled")
print("when given the number of degrees from north and the distance travelled in")
print("a straight line.")
print()
degreesFromNorth = float(input("Please enter the number of degrees from north: ")
distanceInStraightLine = float(input("Please enter the distance travelled in a straight line: "))
#north distance travelled
#work out the sine angle
sineDegrees = 90 - degreesFromNorth
#convert to degrees to radians
sineRadians = math.radians(sineDegrees)
#work out sine
sine = math.sin(sineRadians)
#distance north travelled
distanceNorth = round(sine * distanceInStraightLine,2)
#
#distance east travelled
#convert to radians
sineRadians = math.radians(degreesFromNorth)
#work out sine
sine = math.sin(sineRadians)
#distance east travelled
distanceEast = round(sine * distanceInStraightLine,2)
print()
print("The plane has travelled {0} north.".format(distanceNorth))
print("The plane has travelled {0} east.".format(distanceEast))

    
