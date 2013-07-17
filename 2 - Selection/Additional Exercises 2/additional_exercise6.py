#23-01-2012
#additional exercises 2, program 6
#sample solution

print("OR Gate Simulator")
print("This program asks for the state of two switches and then displays whether the light is")
print("on or not")
print()
switchA = int(input("Please enter the state of switch A (1 or 0): "))
switchB = int(input("Please enter the state of switch B (1 or 0): "))
print()
if switchA == 1 or switchB == 1:
    print("the light is on")
else:
    print("the light is off")
    
