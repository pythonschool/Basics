#2-2-2012
#additional exercise 9
#sample solution

import random,time

guns = []
health = 50
killed = []
#equip with handgun
currentgun = ["Hand Gun",50]

print("Text Based Shooter!")
print("This program is a simple game based on first person shooters where you can pick up and")
print("store weapons and battle enemies...")
print()
print()
anyKey = input("Please press any key to start...")
print()

while health > 0:
    time.sleep(0.25)
    randomNo = random.randint(1,10)
    #print(randomNo)
    print()
    print()
    if randomNo == 1:
        print("There are two Grunts in front of you...")
        print()
        #create grunts (two grunts with 25 health each)
        grunts = [5,5]
        #battle the grunts
        while len(grunts) > 0 and health > 0:
            #current weapon
            print("You are equiped with the {0} ammo:{1}.".format(currentgun[0],currentgun[1]))
            print("There are {0} other guns in your pack.".format(len(guns)))
            print()
            print()
            if len(guns) > 0:
                switch = input("Do you wish to switch gun (Y/N)?: ")
                print()
                #switch gun
                if switch == "Y":
                #display list of guns
                    for item in range(len(guns)):
                      print("{0}. {1} ammo: {2}".format(item+1,guns[item][0],guns[item][1]))
                    selection = int(input("Please select a gun: "))
                    #put current gun in pack
                    if currentgun[1] > 0:
                        guns.append(currentgun)
                    else:
                        print("your {0} was out of ammo, so you have dropped it.".format(currentgun[0]))
                    #get the selected gun
                    currentgun = guns.pop(selection - 1)
                    print("you are now equiped with the {0}".format(currentgun[0]))
                    print()
                    print()
            #decide on firepower
            if currentgun[0] == "Hand Gun":
                firepower = 1
            elif currentgun[0] == "Rifle":
                firepower = 3
            elif currentgun [0] == "Shotgun":
                firepower = 10
            elif currentgun == "Grenade":
                firepower = 20
            print("You bravely battle the grunts...")
            print()
            for count in range(len(grunts)):
              if currentgun[1] > 0:
                  #attack grunt 1
                  hitGrunt = random.randint(1,100)
                  if (hitGrunt % 9) != 0:
                      print("you shot the grunt!")
                      grunts[count] = grunts[count] - firepower
                      #print(grunts[count])
                  else:
                      print("your shot missed...")
                  #decrease ammo
                  currentgun[1] = currentgun[1] - 1
              else:
                   print("You are out of ammo for this gun!!!")
            #remove dead grunts - this is basic list comprehension
            grunts = [each for each in grunts if each > 0]
            #grunts shoot you
            if len(grunts) > 0:
              #each grunt gets a chance to shoot
              for each in grunts:
                  hitYou = random.randint(1,50)
                  if (hitYou % 3) == 0:
                      print("the grunt shot you...")
                      health = health - 1
                  else:
                      print("the grunt missed you...")
            if len(grunts) > 1:
                print("The grunts are still coming for you...")
            elif len(grunts) == 1:
                print("there is only one grunt left...")
            elif len(grunts) == 0:
                print("the grunts are dead...")
                print("your health is now {0}.".format(health))
            print()
            print()
            anyKey = input("Press any key to continue")
    elif randomNo == 2:
        print("A Guard notices you...")
    elif randomNo == 3:
        print("A pack of attack dogs are bounding towards you")
    elif randomNo == 4:
        print("You have encountered a Brute")
    elif randomNo == 5:
        print("There is a health pack to your left")
    elif randomNo == 6:
        print("There is a box of ammo on a shelf")
    elif randomNo == 7:
        print("A shotgun is lying on the floor")
        pickUp = input("Do you want to pick up the shotgun? (Y/N): ")
        if pickUp == 'Y':
            guns.append(["Shotgun",2])
    elif randomNo == 8:
        print("A grenade is over on the table")
    elif randomNo == 9:
        print("You have found a rifle")
