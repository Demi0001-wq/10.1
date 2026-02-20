import psycopg2

# Connection details
conn_params = {
    "host": "sql_db",
    "port": "5432",
    "database": "analysis",
    "user": "simple",
    "password": "qweasd963"
}

# Connect to PostgreSQL
conn = psycopg2.connect(**conn_params)
try:
    with conn.cursor() as cur:
        # 1. Create tables
        # customers: customer_id (5 chars), company_name (up to 100), contact_name (up to 100)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS customers (
                customer_id char(5) PRIMARY KEY,
                company_name varchar(100) NOT NULL,
                contact_name varchar(100) NOT NULL
            );
        """)

        # employees: employee_id (int), first_name (25), last_name (35), title (100), birth_date (date), notes (text - optional)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS employees (
                employee_id int PRIMARY KEY,
                first_name varchar(25) NOT NULL,
                last_name varchar(35) NOT NULL,
                title varchar(100) NOT NULL,
                birth_date date NOT NULL,
                notes text
            );
        """)

        # orders: order_id (int), customer_id (ref), employee_id (ref), order_date (date), ship_city (100)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                order_id int PRIMARY KEY,
                customer_id char(5) REFERENCES customers(customer_id) NOT NULL,
                employee_id int REFERENCES employees(employee_id) NOT NULL,
                order_date date NOT NULL,
                ship_city varchar(100) NOT NULL
            );
        """)

        # 2. Insert data from pre-defined lists
        # Assuming customers_data, employees_data, ordres_data are provided in the environment/script
        
        # Insert customers
        query_customers = "INSERT INTO customers (customer_id, company_name, contact_name) VALUES (%s, %s, %s)"
        cur.executemany(query_customers, customers_data)

        # Insert employees
        query_employees = "INSERT INTO employees (employee_id, first_name, last_name, title, birth_date, notes) VALUES (%s, %s, %s, %s, %s, %s)"
        cur.executemany(query_employees, employees_data)

        # Insert orders (using 'ordres_data' as typed in the prompt)
        query_orders = "INSERT INTO orders (order_id, customer_id, employee_id, order_date, ship_city) VALUES (%s, %s, %s, %s, %s)"
        cur.executemany(query_orders, ordres_data)

    conn.commit()
finally:
    conn.close()
