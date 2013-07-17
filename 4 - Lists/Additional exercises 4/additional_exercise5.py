#6-2-2012
#additional exercise 5
#sample solution

print("TV Schedule")
print("this program stores the schedule for a single tv channel")
print("using a 2D List.")
print()
#empty list
channelSchedule = []
finished = False
channel = input("Which channel are you entering a schedule for: ")
date = input("Which day is the schedule for: ")
while not finished:
    print()
    showName = input("Please enter the show name: ")
    if len(showName) == 0:
        finished = True
    else:
        startTime = input("Please enter the start time for the show: ")
        stopTime = input("Please enter the stop time for the show: ")
        channelSchedule.append([showName,startTime,stopTime])

#display schedule
print()
print("{0} Schedule for {1}".format(channel,date))
print()
print("{0}-{1:<5} {2}".format("Start","Stop","Show"))
finished = False
item = 0
for eachShow in channelSchedule:
    print("{0:<5}-{1:<5} {2}".format(eachShow[1],eachShow[2],eachShow[0]))
    
