#file = open('c.txt', 'r') open the file but need to close the file
import csv

i = 1
file_w = open('d.txt', 'w')
with open('c.txt', 'r') as file:  #no need to close the file
    for line in file:
        writeDate = "line " + str(i) + ":" + line + '\n'
        i+= 1
        file_w(writeDate)

file_w.close()

file_w = open("d.txt", "a")
writeDate = "Tshering Zangmo"
file_w.close()


#csv

with open("staff.csv", newline='', encoding='utf-8-sig') as myCSV:
    data = csv.DictReader(myCSV)
    for r in data:
        print("Phone no :" + r["Phone No"])

record  = ["5555","Hasan","9876778","Wintrop"]

with open("staff.csv", "a", newline='', encoding='utf-8-sig') as myCSV:
    w = csv.writer(myCSV)
    w.writerow(record)
