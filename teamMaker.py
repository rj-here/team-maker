#This is going to be a simple team maker program.
def takeName():
    name = input("What is your name? ") #Takes the name
    print(name)

def playerCount():
    count = input("How many players are involved in total? ") #Takes number of players
    print(count)

def nameSets():
    count = playerCount()
    names = []
    i = 0 #initalize
    while i < count:
        names.__add__(takeName())

nameSets()