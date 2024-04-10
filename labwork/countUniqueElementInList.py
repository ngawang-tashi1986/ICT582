def unique_list(lst):
    uni_list = []

    for i in lst:
        if i not in uni_list:
            uni_list.append(i)

    print(uni_list)
    return len(uni_list)


myList = [1, "cat", 2, "cat", 2.3, 2 ]

listLength = unique_list(myList)
print("The length of unique list is : ", listLength)