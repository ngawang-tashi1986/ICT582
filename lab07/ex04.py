import csv
import os

fileName = "staff.csv"

if os.path.exists(fileName):
    with open(fileName, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader) # to skip the header row
        for row in reader:
            print("Name:", row[1])
            print("Address:", row[3])
else:
    print("The file %s does not exist" % fileName)


