checklist = list()

#simply append strings onto the main checklist
def create(item):
    checklist.append(item)

#returns the places value
def read(index):
    print(checklist[index])
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
        #print(str(index) + list_item)
        print("{} {}".format(index, list_item))
        index += 1

# Mark Complete
def mark_completed(index):
    update(index, "√" + read(index))

def user_input(prompt):
    #the input function displays the prompt
    #and will wait for user_input
    user_input = input(prompt)
    return user_input

# Select code
def select(function_code):
    # we got a lot of work done today
    if function_code == "C":
        input_item = user_input("Input item to add: ")
        create(input_item)
    # read
    elif function_code == "R":
        item_index = int(user_input("Read at which index in list: "))
        # item_index must actually exist or our program will crash.
        read(item_index)
    # Print all items
    elif function_code == "P":
        list_all_items()
    elif function_code == "D":
        user_index = int(user_input("Index to remove: "))
        destroy(user_index)
    elif function_code == "M":
        item_index = int(user_input("Enter index to mark completed: "))
        mark_completed(item_index)
    elif function_code == "U":
        index_item = int(user_input("Enter index to update: "))
        item = user_input("Enter item to update: ")
        update(index_item, item)
    elif function_code == "Q":
        return False
    # Catch all
    else:
        print("Unknown Option")
    return True

running = True
while running:
    selection = user_input(
        "Press C to add to list, R to read from list, U to update list, "
        "\nD to destroy list, P to display full list, M to mark something and Q to quit\n")
    running = select(selection)

def test():
    create('Red Shoes')
    create('Blue Socks')
    create('Pink Shirt')

    update(0,'Red Shoes ')
    update(1,'Orange Hat')
    update(2,'Pink Shirt ')

    destroy(0)
    
    print(read(0))
    list_all_items()
    mark_completed(0)

    print(read(0))

test()
