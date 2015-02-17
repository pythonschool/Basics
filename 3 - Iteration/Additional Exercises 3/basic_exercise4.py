#25-01-2012
#additional exercises 3, question 4
#sample solution

import time

print("Count down")
print("This program counts down from 10 to 0")
print("indicating how long there is to go before time runs out")
print()
for timeCount in range(10,0,-1):
    print("{0:>2} seconds remaining!".format(timeCount))
    time.sleep(1)
print()
print("YOUR TIME IS UP!!!!!")
