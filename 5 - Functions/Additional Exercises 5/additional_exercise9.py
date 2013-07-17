#2-2-2012
#additional exercise 9
#sample solution

import random,time

def initialSetUp():
    guns = []
    health = 50
    killed = []
    #equip with handgun
    currentgun = ["Hand Gun",50]
    return guns,health,killed,currentgun


def displayInfo():
    print("Text Based Shooter!")
    print("This program is a simple game based on first person shooters where you can pick up and")
    print("store weapons and battle enemies...")
    print()
    print()
    anyKey = input("Please press any key to start...")
    print()


def displayGuns(guns):
    #display list of guns
    for item in range(len(guns)):
      print("{0}. {1} ammo: {2}".format(item+1,guns[item][0],guns[item][1]))
      
def selectGun(guns,currentgun):
    displayGuns(guns)
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
    return currentgun


def setFirepower(currentgun):
    #decide on firepower
    if currentgun[0] == "Hand Gun":
        firepower = 1
    elif currentgun[0] == "Rifle":
        firepower = 3
    elif currentgun [0] == "Shotgun":
        firepower = 10
    elif currentgun == "Grenade":
        firepower = 20
    return firepower

def switchGuns(guns,currentgun):
    if len(guns) > 0:
        switch = input("Do you wish to switch gun (Y/N)?: ")
        print()
        #switch gun
        if switch == "Y":
            currentgun = selectGun(guns,currentgun)
    firepower = setFirepower(currentgun)
    return firepower

def battleGrunt(grunt,currentgun,firepower):
    if currentgun[1] > 0:
      #attack grunt 1
      hitGrunt = random.randint(1,100)
      if (hitGrunt % 9) != 0:
          print("you shot the grunt!")
          grunt = grunt - firepower
          #print(grunts[count])
      else:
          print("your shot missed...")
      #decrease ammo
      currentgun[1] = currentgun[1] - 1
    else:
       print("You are out of ammo for this gun!!!")
    return grunt

def removeDeadEnemies(enemies):
    #remove dead grunts - this is basic list comprehension
    enemies = [each for each in enemies if each > 0]
    return enemies

def gruntAttack(health,grunts):
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
    return health

def analysisOfBattlefield(enemies,enemyname,health):
    if len(enemies) > 1:
        print("The {0}s are still coming for you...".format(enemyname))
    elif len(enemies) == 1:
        print("there is only one {0} left...".format(enemyname))
    elif len(enemies) == 0:
        print("the {0}s are dead...".format(enemyname))
        print("your health is now {0}.".format(health))
    print()
    print()

def battleGrunts(guns,currentgun,health):
    print("There are two Grunts in front of you...")
    print()
    #create grunts (two grunts with 5 health each)
    grunts = [5,5]
    #battle the grunts
    while len(grunts) > 0 and health > 0:
        #current weapon
        print("You are equiped with the {0} ammo:{1}.".format(currentgun[0],currentgun[1]))
        print("There are {0} other guns in your pack.".format(len(guns)))
        print()
        print()
        #offer chance to switch gun and get the firepower of the selected gun
        firepower = switchGuns(guns,currentgun)
        #battle each grunt
        for count in range(len(grunts)):
             grunts[count] = battleGrunt(grunts[count],currentgun,firepower)
        grunts = removeDeadEnemies(grunts)
        health = gruntAttack(health,grunts)
        analysisOfBattlefield(grunts,"grunt",health)
        print()
        print()
        anyKey = input("Press any key to continue")
    return health
        
def pickUpGun(guns,guntype):
    print("A {0} is lying on the floor".format(guntype))
    pickUp = input("Do you want to pick up the {0}? (Y/N): ".format(guntype))
    if pickUp == 'Y':
        guns.append([guntype,random.randint(1,10)]) 
         
        
def playGame(setUpValues):
    guns = setUpValues[0]
    health = setUpValues[1]
    killed = setUpValues[2]
    currentgun = setUpValues[3]
    while health > 0:
        time.sleep(0.25)
        randomNo = random.randint(1,10)
        #print(randomNo)
        print()
        print()
        if randomNo == 1:
            health = battleGrunts(guns,currentgun,health)
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
            pickUpGun(guns,"Shotgun")
        elif randomNo == 8:
            print("A grenade is over on the table")
        elif randomNo == 9:
            print("You have found a rifle")
    print()
    print("You are now dead! Thanks for playing!")


def firstPerson():
    displayInfo()
    setUpValues = initialSetUp()
    playGame(setUpValues)
