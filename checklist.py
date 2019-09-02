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
    checklist[index] = ("√" + checklist[index])

def test():
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")
    destroy(1)

    print(read(0))
    #print(read(1))

test()
print (checklist[1])
mark_completed(1)
print (checklist[1])

list_all_items()
