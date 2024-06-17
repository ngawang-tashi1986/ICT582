import sys
from utility import *

customers_db = []
sales_db = []

args = sys.argv[1:]

if len(args) == 2:
    customers_db, sales_db = load_csv_data(args[0], args[1])

print(f"\n{'Western Wholesales Pty Ltd':^120}")    

while True:   
    line_style_underscore(120)
    print(f"{bold_text("M A I N    M E N U"):^120}")
    line_style_hyphen(120)
    print(f"{'1. Load customer and sales records': <40}  {'2. Save customer records to a CSV file':40} {'3. Save sale records to a CSV file':40}")
    print(f"{'4. Quit':40}")
    line_style_underscore(120)

    choice = input("\nEnter your choice : ")
    
    if choice == '1':
        customer_filename = input("Enter customer file name      : ")
        customers_db = load_csv_data(customer_filename, 'Customers')
        
        sales_filename = input("Enter sales file name         : ")
        sales_db = load_csv_data(sales_filename, 'Sales')
    elif choice == '2':
        customer_filename = input("Enter customer file name      : ")
        save_customers(customer_filename,customers_db)

    elif choice == '3':
        sales_filename = input("Enter sales file name      : ")
        save_sales(sales_filename,sales_db)
        
    elif choice == '4':
        print("Exiting Program !!!")
        break
    else:
        print("Invalid choice. Please try again !!!")
    

        
