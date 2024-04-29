import csv
import os

fileName = "staff.csv"

# Function to add new staff
def add_staff():
    with open(fileName, mode='a', newline='') as file:
        writer = csv.writer(file)

        # Ask the user for the new staff  details
        staff_id = int(input('Enter the staff id           : '))
        name = input('Enter the staff name         : ')
        phone_number = input('Enter the staff phone number : ')
        home_address = input('Enter the staff home address : ')
                    
        # Add the details to the CSV file
        writer.writerow([staff_id, name, phone_number, home_address])
        print('Staff details added successfully!\n')

# Display a menu
def display_menu():
    while True:
        print('1. Add a new staff member')
        print('2. Stop')
        choice = input('Enter your choice: ')
            
        if choice == '1':
            add_staff()
        elif choice == '2':
            print('Thank You!')
            break
        else:
            print('Invalid choice. Please try again.\n')

if os.path.exists(fileName):
    display_menu()
else:
    print("The file %s does not exist" % fileName)







    


