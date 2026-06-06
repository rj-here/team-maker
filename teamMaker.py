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
    style = int(input("What's the preferred team configuration?\nIf a set # of teams -> 1, If a set # of players per team -> 2, Other -> 3\n"))
    if style == 1:
        noOfTeams(names)
    elif style == 2:
        pplPerTeam(names)
    elif style == 3:
        other(names)
    else:
        print("Invalid input! Try again.")
        teamConfig(names)

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

def other(names):
    print("Ok. Not fully randomized then? How do we do this?")
    print("1: Certain players may not be on the same team, 2: Certain players must be on the same team")
    choice = int(input("Enter your choice (1 or 2): "))
    if choice == 1:
        other1(names)
    elif choice == 2:
        other2(names)

def other1(names):
    print("Ok. Who can't be on the same team?")
    namesNotTogether = set(input("Enter names separated by commas: ").split(","))
    #separate names by those that cannot be and can be together, Gemini guides
    notInSameTeam = [name for name in namesNotTogether if name in names]
    canBeTogether = [name for name in names if name not in namesNotTogether]
    print("Got it.")
    teamCount = int(input("How many teams do you want?"))
    teams = [[] for counter in range(teamCount)] #initialize teams
    #First, put the "not together" names in different teams, Gemini guides
    for i, name in enumerate(notInSameTeam):
        teams[i % teamCount].append(name)
    #Then, shuffle the "can be together" names and distribute them randomly, Gemini guides
    random.shuffle(canBeTogether)
    for i, name in enumerate(canBeTogether):
        teams[i % teamCount].append(name)
    printTeams(teams=teams)

def other2(names):
    print("Ok, what are the combinations that must be together?")
    #separate names by those that must be together and those that can be together
    togetherGroups = set(input("Enter names separated by commas, with | to separate groups ").split("|"))
    #initializing teams
    teamCount = int(input("How many teams do you want?"))
    teams = []
    for group in togetherGroups:
        groupNames = set(group.split(","))
        if groupNames:
            teams.append(groupNames)
    #Now, shuffle the remaining names and distribute them randomly
    remaining_names = [name for name in names if all(name not in group for group in teams)]
    random.shuffle(remaining_names)
    for i, name in enumerate(remaining_names):
        teams[i % teamCount].append(name)
    printTeams(teams=teams)
    

def printTeams(teams):
    for team in teams:
        print(f"Team {team}")

teamConfig(names=nameSet())