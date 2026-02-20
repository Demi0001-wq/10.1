import csv
import psycopg2

# 1. Load data from CSV files
def load_csv(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        # Use DictReader to skip headers and handle quotes easily
        reader = csv.reader(f)
        next(reader) # Skip header
        return list(reader)

# Loading the data (Assuming files are in the same directory as the script)
customers_data = load_csv('customers_data.csv')
employees_raw = load_csv('employees_data.csv')
ordres_data = load_csv('orders_data.csv') # Using "ordres_data" as per prompt

# The employees schema requires an employee_id (int). 
# Since the CSV doesn't have it, we generate it (1, 2, 3...)
employees_data = []
for i, row in enumerate(employees_raw, 1):
    # row is: [first_name, last_name, title, birth_date, notes]
    # we need: [employee_id, first_name, last_name, title, birth_date, notes]
    employees_data.append([i] + row)

# 2. Database connection parameters
conn_params = {
    "host": "sql_db",
    "port": "5432",
    "database": "analysis",
    "user": "simple",
    "password": "qweasd963"
}

# 3. Connect and perform operations
conn = psycopg2.connect(**conn_params)
try:
    with conn.cursor() as cur:
        # Create Tables
        cur.execute("""
            CREATE TABLE IF NOT EXISTS customers (
                customer_id char(5) PRIMARY KEY,
                company_name varchar(100) NOT NULL,
                contact_name varchar(100) NOT NULL
            );
            
            CREATE TABLE IF NOT EXISTS employees (
                employee_id int PRIMARY KEY,
                first_name varchar(25) NOT NULL,
                last_name varchar(35) NOT NULL,
                title varchar(100) NOT NULL,
                birth_date date NOT NULL,
                notes text
            );
            
            CREATE TABLE IF NOT EXISTS orders (
                order_id int PRIMARY KEY,
                customer_id char(5) REFERENCES customers(customer_id) NOT NULL,
                employee_id int REFERENCES employees(employee_id) NOT NULL,
                order_date date NOT NULL,
                ship_city varchar(100) NOT NULL
            );
        """)

        # Insert Data
        cur.executemany("INSERT INTO customers VALUES (%s, %s, %s)", customers_data)
        cur.executemany("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)", employees_data)
        cur.executemany("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)", ordres_data)

    conn.commit()
finally:
    conn.close()
