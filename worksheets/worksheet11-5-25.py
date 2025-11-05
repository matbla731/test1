#function 1 add task, inputs list and item
def append(Answerofquestion1):
    ListA.append(Answerofquestion1)

# function 2 print all tasks list
def printTasks():
    print("___Tasks___")

    for item in ListA:
        print(ListA.index(item)+1," - ", item)

    for i in range(0, len(ListA)):
        print(i, "- ", ListA[i])

# function 3 remove oldest added task on list
def removeOldest():
    ListA.pop(0)

#create list
ListA=[]
"""
would you like to 1- add a task, 2- remove the 1st item 3- see your tasks

if 1
what would you like to add

~ adds task

elif 2
~ removes task

elif 3
~ see tasks

else
incorrect input
"""

# while loop
running = False
while running: 

    # ask user if they want to add task, remove oldest, print tasks
    whatEvent=input("would you like to 1- add a task, 2- remove the 1st item 3- see your tasks")

    # if (if,elif,else) statement
    if whatEvent == "1":
        Answerofquestion1 = input("what would you like to add to tasks")
        append(Answerofquestion1)

    elif whatEvent == "2":
        removeOldest()
        
    elif whatEvent == "3":
        printTasks()

    else:
        print("error")
