#This is going to be a simple team maker program.
def takeNames(peopleCount):
    #This function takes in names
    listOfNames = [] #List of names.
    while len(listOfNames < peopleCount):
        name = input("Please put in a name.")
        listOfNames.__add__(name)

takeNames(5)
