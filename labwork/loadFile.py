file = open("a.txt")

print(file)  # display the file information

print(file.read()) # read the file

print(file.read(5)) # read first 5 line of the file

# read all the line
for line in file:
    print(line, end='')


for line in file:
    con = line.split()
    print(con[1])


file = open("b.txt")
file_w = open("c.txt", "w")
for line in file:
    con = line.split(',')
    avgMark = ((float(con[2]) + float(con[3]) + float(con[4]))/3.0)
    print("The average is ", avgMark)
    print("Name " + con[1], + " Final mark : " + con[4])    
    writeDate = str(avgMark) + "\n"
    file_w.write(writeDate)    # write average in another file with new line

file.close()
file_w.close()