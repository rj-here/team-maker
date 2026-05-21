#This is going to be a simple team maker program.
def takeName(count):
    names = set()
    for i in range(0, count): 
        #Don't be rusty | https://wiki.python.org/python/ForLoop.html
        name = input("What is your name? ") #Takes the name
        names.add(name)
    return names

def playerCount():
    count = int(input("How many players are involved in total? ")) #Takes number of players
    print(f"${count} players involved.")
    return count

def nameSets():
    count = playerCount()
    print(count)
    names = takeName(count)

def teamCount():
    team = int(input("How many teams do you want? ")) #Number of teams
    return team

nameSets()
teamCount()