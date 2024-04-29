import csv
import sys
import os

#def load_csv(filename):
#    with open(filename, mode='r', newline='', encoding='utf-8') as file:
#        reader = csv.DictReader(file)
#        return list(reader)
    
def load_csv(filename):
    csv_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(csv_dir, filename)
    with open(file_path,'r', newline='', encoding='utf-8') as file:
        content = file.read()
    return content

#def save_csv(filename, fieldnames, data):
#    if os.path.exists(filename):
#        response = input(f"File '{filename}' already exists. Overwrite it? (yes/no): ")
#        if response.lower() != 'yes':
#            print("Operation canceled.")
#            return
#    with open(filename, mode='w', newline='', encoding='utf-8') as file:
#        writer = csv.DictWriter(file, fieldnames=fieldnames)
#        writer.writeheader()
#        writer.writerows(data)
#        print(f"Data has been saved to {filename}")


def save_csv(filename, fieldnames, data):
    csv_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(csv_dir, filename)

    if os.path.exists(filename):
        response = input(f"File '{filename}' already exists. Overwrite it? (yes/no): ") 
        if response.lower() != 'yes':
            print("Operation canceled.")
            return
#    with open(filename, mode='w', newline='', encoding='utf-8') as file:
#        writer = csv.DictWriter(file, fieldnames=fieldnames)
#        writer.writeheader()
#        writer.writerows(data)
#        print(f"Data has been saved to {filename}")
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(data)
        print(f"Data has been saved to {filename}")

def load_data(customers_filename, sales_filename):
    customers = load_csv(customers_filename)
    sales = load_csv(sales_filename)
    return customers, sales

def save_customers_to_csv(customers):
    if not customers:
        print("No customer records in memory.")
        return
    filename = input("Enter filename to save customers: ")
    save_csv(filename, ['cust_id', 'name', 'postcode', 'phone'], customers)

def save_sales_to_csv(sales):
    if not sales:
        print("No sales records in memory.")
        return
    filename = input("Enter filename to save sales: ")
    save_csv(filename, ['date', 'trans_id', 'cust_id', 'category', 'value'], sales)


customers = []
sales = []

args = sys.argv[1:]
if len(args) == 2:
    customers, sales = load_data(args[0], args[1])

while True:
    print("\nMenu:")
    print("1. Load customer and sales records")
    print("2. Save customer records to a CSV file")
    print("3. Save sales records to a CSV file")
    print("4. Quit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        customers_filename = input("Enter the customer records filename: ")
        sales_filename = input("Enter the sales records filename: ")
        customers, sales = load_data(customers_filename, sales_filename)
        print("Data loaded successfully.")
    elif choice == '2':
        save_customers_to_csv(customers)
    elif choice == '3':
        save_sales_to_csv(sales)
    elif choice == '4':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")

