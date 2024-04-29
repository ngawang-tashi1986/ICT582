import os

fileName = "ex03.txt"

# Function to get the initial size of the file
def get_file_size():   
    return os.path.getsize(fileName)

# Function to append the first two line
def append_to_file():
    with open(fileName, 'r') as file:
        content = file.readlines()

    if len(content) >= 2:
        first_two_lines = content[:2]
    else:
        first_two_lines = content  # If the file has less than 2 lines, take what is there

    with open(fileName, 'a') as file:
        file.writelines(first_two_lines)

# Function to read the first three line
def read_three_line():
    print("The first three lines are : ")
    with open(fileName, 'r') as f:
        for i in range(3):
            line = f.readline()
            if line == '':
                break
            print(line, end='') 

# Function to get the new size after appending the line
def get_new_size():
    with open(fileName, 'r') as file:
        content = file.read()
    new_size = len(content)
    print(f"\nNew size of the file: {new_size} bytes")



if os.path.exists(fileName):
    initial_size = get_file_size()
    print("Initial size of %s: %s bytes" % (fileName, initial_size))
    append_to_file()   
    read_three_line()
    get_new_size()
else:
    print("The file %s does not exist" % fileName)

