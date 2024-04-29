fileName = "D:/Murdoch Uni/ICT582/lab07/ex01.txt"

i = 1
with open(fileName, 'r') as file:
    for line in file:
        print("line " + str(i) + ":" + line, end='' )
        i+=1
