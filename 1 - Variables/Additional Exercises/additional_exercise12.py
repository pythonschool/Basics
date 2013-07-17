#16-01-2012
#additional exercise 12
#sample solution

import math

print("Balloon Height")
print("This program calculates how high a balloon has reached")
print("when given the number of degrees the string makes with the horizontal")
print("and the length of the string")
print()
degreesFromHorizontal = float(70)
lengthOfString = float(120)
#degrees in radians
radiansFromHorizontal = math.radians(degreesFromHorizontal)
#sine
sine = math.sin(radiansFromHorizontal)
balloonHeight = round(sine * lengthOfString,2)
print("The balloon is {0} in the air.".format(balloonHeight))


    
