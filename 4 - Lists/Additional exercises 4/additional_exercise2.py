#2-2-2012
#additional exercise 2
#sample solution

print("TV Schedule")
print("this program stores the schedule for a single tv channel")
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
        channelSchedule.append(showName)
        channelSchedule.append(startTime)
        channelSchedule.append(stopTime)

#display schedule
print()
print("{0} Schedule for {1}".format(channel,date))
print()
print("{0}-{1:<5} {2}".format("Start","Stop","Show"))
finished = False
item = 0
while not finished:
    if item+2 <= len(channelSchedule):
        print("{0:<5}-{1:<5} {2}".format(channelSchedule[item+1],channelSchedule[item+2],channelSchedule[item]))
        item = item + 3
    else:
        finished= True
    
