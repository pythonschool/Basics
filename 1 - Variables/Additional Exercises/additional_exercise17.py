#16-01-2012
#additional exercise 12
#sample solution

import math

print("Distance Climbed")
print("This program calculates how much height is gained when travelling a")
print("given distance and an incline angle")
print()
distanceTravelled = float(input("Please enter the distance travelled: "))
inclineAngle = float(input("Please enter the incline angle: "))
#convert degrees to radians
inclineRadians = math.radians(inclineAngle)
#get the sine
sine = math.sin(inclineRadians)
#calculate height
height = round(distanceTravelled * sine,2)
print()
print("The distance travelled horizontally is {0}".format(height))


    
