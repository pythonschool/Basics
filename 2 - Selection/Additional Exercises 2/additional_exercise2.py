#23-01-2012
#additional exercises 2, program 2
#sample solution

print("Travelling Time")
print("This program asks for a distance and whether you will")
print("travelling on motorway, a-road or through town and then")
print("tells you how long the journey will take.")
print()
Distance = float(input("Please enter the distance to travel (miles): "))
print()
print("Road Types")
print("M = Motorway")
print("A = A Road")
print("T = Travelling through town")
roadType = input("Please enter the type of road travelling on (M or A or T): ")
print()
if roadType == 'M':
    time = Distance/70
elif roadType == 'A':
    time = Distance/60
elif roadType == 'T':
    time = Distance/30
else:
    print("You entered an invalid road type")
if roadType == 'M' or roadType == 'A' or roadType == 'T':
    print("The time taken to travel {0} miles will be {1} hours".format(Distance,round(time,2)))    
    
