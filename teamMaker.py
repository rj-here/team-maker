#This is going to be a simple team maker program.
import random #https://docs.python.org/3/library/random.html | https://www.w3schools.com/Python/module_random.asp
def takeName(count):
    names = set()
    for i in range(0, count): 
        #Don't be rusty | https://wiki.python.org/python/ForLoop.html
        name = input("What is your name? ") #Takes the name
        names.add(name)
    return names

def playerCount():
    count = int(input("How many players are involved in total? ")) #Takes number of players
    print(f"{count} players involved.")
    return count

def nameSet():
    count = playerCount()
    print(count)
    names = takeName(count)
    return names

def teamConfig(names):
    style = int(input("Do you want a certain number of teams, or certain number of people per team?\nIf # of teams -> 1, If # of players per team -> 2\n"))
    if style == 1:
        noOfTeams(names)
    elif style == 2:
        pplPerTeam()

def noOfTeams(names):
    if not names: #Gemini guided | https://www.w3schools.com/python/gloss_python_if_not.asp
        print("No names found!")
        return None
    names = list(names) #Gemini guided | https://www.w3schools.com/python/python_lists.asp
    random.shuffle(names) 
    teamCount = int(input("How many teams do you want?"))
    teams = [[] for counter in range(teamCount)] #Gemini guided | https://www.geeksforgeeks.org/python/declare-an-empty-list-in-python/ | https://www.geeksforgeeks.org/python/nested-list-comprehensions-in-python/

    for i, name in enumerate(names): #https://www.geeksforgeeks.org/python/enumerate-in-python/
        teams[i % teamCount].append(name)
    printTeams(teams=teams)

def pplPerTeam(names):
    random.shuffle(names) #shuffle

    #Validate input
    minPpl = int(input("How many people do you want per team? (Minimum)")) 
    maxPpl = int(input("How many people do you want per team? (Maximum)"))
    while (minPpl > maxPpl):
        print("Try again!")
        minPpl = int(input("How many people do you want per team? (Minimum)")) 
        maxPpl = int(input("How many people do you want per team? (Maximum)"))
    
    teams = [] #initialize

    #Create teams until names ain't finished, Gemini guides.
    remaining_names = names[:]
    while(len(remaining_names) > 0):
        #Size of teams:
        size = random.randint(minPpl, maxPpl)
        #Just keeping track: not taking more names than leftovers
        actualSize = min(size, len(remaining_names))

        #Slice it for a team
        team = remaining_names[:actualSize]
        teams.append(tuple(team))

        #Remove those names from the pool
        remaining_names = remaining_names[:actualSize]
    printTeams(teams=teams)

def printTeams(teams):
    for team in teams:
        print(f"Team {team}")

teamConfig(names=nameSet())