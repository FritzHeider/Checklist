checklist = list()

#simply append strings onto the main checklist
def create(item):
    checklist.append(item)

#returns the places value
def read(index):
    return checklist[index]


#takes two parameters one for the placement and the second with the change
def update(index, item):
    checklist[index] = item


#regularly pops off the end of the list unless specified
def destroy(index):
    checklist.pop(index)

#it wanted to make sure i had the index listed as a stirng
def list_all_items():
    index = 0
    for list_item in checklist:
        print(str(index) + list_item)
        print("{} {}".format(index, list_item))
        index += 1


#this was very tricky for the all the logic behind it but i truly think i understand it now
def mark_completed(index):
    item = checklist[index]

    if item[0] != "√" :
        checklist[index] = "√ " + checklist[index]
        return("\nCheck Marked.")
    else:
        return('\nAlready marked complete')

def mark_incomplete(index):
    item = checklist[index]

    if item[0] == "√":
        incompleted_item = item.replace("√ ", "")
        checklist[index] = incompleted_item
        return("\n Marked Incomplete.")
    else:
        return("\n Already Marked Incomplete.")

def list_all_items():
    index = 0
    for list_item in checklist:
        #print(str(index) + list_item)
        print("{} {}".format(index, list_item))
        index += 1

def user_input(prompt):
    #the input function displays the prompt
    #and will wait for user_input
    user_input = input(prompt)
    return user_input


def select(function_code):
    if function_code == "C":
        item = user_input("Name item you would like to create >")
        create(item)
        return True
    elif function_code == "R":
        index = user_input("Which index would you like to read? ")

        print(read(index))
        return True
    elif function_code == "P":
        list_all_items()
        return True
    elif function_code == "Q":
        return False
    else:
        print("Unknown Option")
    return True

def test():
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")

    destroy(

    print(read(0))

    #list_all_items()

    #user_value = user_input("Please enter a value> ")
    #print(user_value)

running = True
while running:
        selection = user_input(
            "Press C to add to the list, R to Read from the list and P to diplay the list"
        )
        select(selection)
