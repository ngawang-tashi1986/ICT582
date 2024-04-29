import os


# The following methods load the csv from the current working directory.
# The methods takes in file name of the csv file.
def load_csv_file(fileName):
    current_working_dir = os.path.dirname(os.path.abspath(__file__)) # Get current working directory
    file_path = os.path.join(current_working_dir, fileName)
    with open(file_path, 'r', newline='', encoding='utf-8') as file:
        content = file.read()
    return content

def load_csv_data(customers_csv, sales_csv):
    customers = load_csv_file(customers_csv)
    sales = load_csv_file(sales_csv)
    return customers, sales
