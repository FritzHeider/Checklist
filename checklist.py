checklist = list()

def create(item):
    checklist.append(item)

def read(index):
    return checklist[index]

def update(index, item):
    checklist[index] = item

def destroy(index):
    checklist.pop(index)

def list_all_items():
    index = 0
    for list_item in checklist:
        print(str(index) + list_item)
        print("{} {}".format(index, list_item))
        index += 1

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

def test():
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")
    destroy(1)
    mark_completed(0)
    print(checklist)

test()
