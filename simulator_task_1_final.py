import csv
import psycopg2

# 1. Loading data (matching the simulator's pre-load logic)
with open('customers_data.csv', newline='', encoding='utf-8') as file:
    customers_data = [row for row in csv.reader(file) if 'customer_id' not in row]

with open('employees_data.csv', newline='', encoding='utf-8') as file:
    employees_data = [row for row in csv.reader(file) if 'first_name' not in row]

with open('orders_data.csv', newline='', encoding='utf-8') as file:
    orders_data = [row for row in csv.reader(file) if 'order_id' not in row]

# 2. Database connection
conn = psycopg2.connect(
    host="sql_db",
    port="5432",
    database="analysis",
    user="simple",
    password="qweasd963"
)
cur = conn.cursor()

# 3. Required cleanup and schema setup (DO NOT DELETE)
cur.execute("create schema if not exists itresume18169;")  
cur.execute("SET search_path TO itresume18169;")
cur.execute("DROP TABLE IF EXISTS orders")
cur.execute("DROP TABLE IF EXISTS customers")
cur.execute("DROP TABLE IF EXISTS employees")

# 4. Create tables
cur.execute("""
    CREATE TABLE customers (
        customer_id char(5) PRIMARY KEY,
        company_name varchar(100) NOT NULL,
        contact_name varchar(100) NOT NULL
    );
""")
cur.execute("""
    CREATE TABLE employees (
        employee_id int PRIMARY KEY,
        first_name varchar(25) NOT NULL,
        last_name varchar(35) NOT NULL,
        title varchar(100) NOT NULL,
        birth_date date NOT NULL,
        notes text
    );
""")
cur.execute("""
    CREATE TABLE orders (
        order_id int PRIMARY KEY,
        customer_id char(5) REFERENCES customers(customer_id) NOT NULL,
        employee_id int REFERENCES employees(employee_id) NOT NULL,
        order_date date NOT NULL,
        ship_city varchar(100) NOT NULL
    );
""")
conn.commit() # Save table structure

# 5. Insert Customers
for row in customers_data:
    cur.execute("INSERT INTO customers (customer_id, company_name, contact_name) VALUES (%s, %s, %s) RETURNING *", row)

# Verification line (DO NOT DELETE)
conn.commit()
res_customers = cur.fetchall()

# 6. Insert Employees (adding ID since it's missing in CSV but required by schema)
for i, row in enumerate(employees_data, 1):
    # row is [first_name, last_name, title, birth_date, notes]
    data = [i] + row
    cur.execute("INSERT INTO employees (employee_id, first_name, last_name, title, birth_date, notes) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *", data)

# Verification line (DO NOT DELETE)
conn.commit()
res_employees = cur.fetchall()

# 7. Insert Orders
for row in orders_data:
    cur.execute("INSERT INTO orders (order_id, customer_id, employee_id, order_date, ship_city) VALUES (%s, %s, %s, %s, %s) RETURNING *", row)

# Verification line (DO NOT DELETE)
conn.commit()
res_orders = cur.fetchall()

# 8. Cleanup
cur.close()
conn.close()
