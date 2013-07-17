#23-01-2012
#additional exercises 2, program 1
#sample solution

print("Volumes")
print("This program asks for dimensions of both a fridge and a lift")
print("then it works out how much volume remains inside the lift once the")
print("fridge is inside.")
print("It also tells you whether the fridge will fit in the lift")
print()
liftW = float(input("Please enter the width of the lift: "))
liftH = float(input("Please enter the height of the lift: "))
liftD = float(input("Please enter the depth of the lift: "))
print()
fridgeW = float(input("please enter the width of the fridge: "))
fridgeH = float(input("please enter the height of the fridge: "))
fridgeD = float(input("please enter the depth of the fridge: "))
print()
liftV = liftW * liftH * liftD
fridgeV = fridgeW * fridgeH * fridgeD
liftSpace = liftV - fridgeV
print("The lift's volume is {0}.".format(liftV))
print("The fridge's volumne is {0}.".format(fridgeV))
print("The lift has {0} of remaining space.".format(liftSpace))
#extension for additional exercises 2
width = liftW > fridgeW
height = liftH > fridgeH
depth = liftD > fridgeD
print()
if width and height and depth:
    print("the fridge will fit in the lift")
else:
    print("the fridge will not fit in the lift as it is:")
    if not width:
        print("to wide")
    if  not height:
        print("to tall")
    if not depth:
        print("to deep")
    
    
