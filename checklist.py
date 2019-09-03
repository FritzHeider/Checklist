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
        print(str(index) + list_item)
        index += 1


def test():
    create("socks")
    create("shoes")
    list_all_items()

test()

print(checklist)
