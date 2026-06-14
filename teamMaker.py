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
    names = list(names) #GitHub Copilot to the rescue
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
        #Configuring team size, GitHub Copilot suggests
        remaining_count = len(remaining_names)

        possible_sizes = [
            size for size in range(minPpl, min(maxPpl, remaining_count) + 1) #GitHub Copilot suggests | takes a range and ensures the size isn't weird (so for 3-4 per team, there isn't a solo)
            if remaining_count - size == 0 or remaining_count - size >= minPpl
        ]

        if not possible_sizes:
            print("Cannot split remaining players with those bounds.")
            break

        actualSize = random.choice(possible_sizes)

        #Slice it for a team
        team = remaining_names[:actualSize] #GitHub Copilot suggests
        teams.append(tuple(team))

        #Remove those names from the pool
        remaining_names = remaining_names[actualSize:]
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
    raw_input = input("Enter names separated by commas: ")
    restricted_names = [name.strip() for name in raw_input.split(",") if name.strip()] #GitHub Copilot suggests | takes the input, splits by comma, and removes extra spaces. Also ensures no empty names are added.
    restricted_names = [name for name in restricted_names if name in names] #GitHub Copilot suggests | ensures that the restricted names are actually in the list of names provided. If not, it removes them from the restricted list.

    print("Got it.")
    team_count = int(input("How many teams do you want?"))
    teams = [[] for counter in range(team_count)]

    if len(restricted_names) > team_count:
        print("Too many restricted players for the number of teams.")
        return

    # Put the restricted names into different teams first.
    for i, name in enumerate(restricted_names):
        teams[i % team_count].append(name)

    # Randomly assign everyone else.
    remaining_names = [name for name in names if name not in restricted_names]
    random.shuffle(remaining_names)

    for name in remaining_names:
        target_team = min(teams, key=len)
        target_team.append(name)

    printTeams(teams=teams)

def other2(names):
    print("Ok, what are the combinations that must be together?")
    raw_input = input("Enter groups separated by |, with names separated by commas: ") #GitHub Copilot suggests | takes the input, splits by | for groups, then splits by comma for names, and removes extra spaces. Also ensures no empty names are added.

    groups = [] #initialize
    for part in raw_input.split("|"): #GitHub Copilot suggests | splits the input into groups by |, then processes each group to extract names.
        group = [name.strip() for name in part.split(",") if name.strip()] #GitHub Copilot suggests | takes each group, splits by comma for names, removes extra spaces, and ensures no empty names are added.
        group = [name for name in group if name in names] #GitHub Copilot suggests | ensures that the names in the group are actually in the list of names provided. If not, it removes them from the group.
        if group:
            groups.append(group)

    team_count = int(input("How many teams do you want?"))
    teams = [[] for _ in range(team_count)]

    if len(groups) > team_count:
        print("Too many grouped players for the number of teams.")
        return

    # Place each required group into a different team.
    for i, group in enumerate(groups):
        teams[i % team_count].extend(group)

    # Put the remaining players randomly.
    remaining_names = [name for name in names if all(name not in group for group in groups)]
    random.shuffle(remaining_names)

    for name in remaining_names:
        target_team = min(teams, key=len)
        target_team.append(name)

    printTeams(teams=teams)
    
def printTeams(teams):
    for team in teams:
        print(f"Team {team}")

names = nameSet()
teamConfig(names)