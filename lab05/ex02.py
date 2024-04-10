# The following program takes a list as its parameter and returns the
# number of unique elements from original list and display the new list with unique elements.

def countUnique(list):
    tempList = []
    for x in list:
        if x not in tempList:
            tempList.append(x)
    return (len(tempList), tempList)

list = []
while True:
    val = input("Enter something do add into the list or 'stop' to stop entering: ")
    if val == "stop":
        uniqueTuple = countUnique(list)
        print("The original list is ", list)
        print("There are %s unique elements in %s" % (uniqueTuple[0], uniqueTuple[1]))
        break
    else:
        list.append(val)
