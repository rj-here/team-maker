#This is going to be a simple team maker program.
import random
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

def nameSet():
    count = playerCount()
    print(count)
    names = takeName(count)

def teamCount():
    team = int(input("How many teams do you want? ")) #Number of teams
    return team

def teamSizeFixed():
    fixed = (input("Does the team size need to be fixed? For example, a team of 11 to play cricket :)"))
    if (fixed == "Yes" or "True"):
        fixed = True
    
    elif (fixed == "No" or "False"):
        fixed = False
    
    return fixed

def combinationType():
    print('Which type of combination do you want?')
    print('1: Fully randomized!')
    print('2: Separating select players')
    print('3: Certain combinations (1 mentor, 2 volunteers, 2 juniors, as an example)')
    combination = int(input("Please provide the choice between the 3! "))
    if (combination == 1):

def randomize(names, teamSize, teamCount):
    random.shuffle(names) #Shuffle - https://www.geeksforgeeks.org/python/random-shuffle-function-in-python/
    teams = set() #Gemini guides!

    for i in range(0, len(names), teamSize): #adding all names to teams until done
        chunk = names[i : i + teamSize] #making a chunk to add set of teams
        teams.add(tuple(chunk)) #add to team
    return teams

        
def selectSeparationFirst(names, teamSize, teamCount):

def certainCombos(names, teamSize, teamCount):

        
nameSet()
teamCount()
teamSizeFixed()
combinationType()