import sqlite3
import pandas as pd

# 1. Connect to Database (This creates a file named 'store.db')
conn = sqlite3.connect('store.db')
cursor = conn.cursor()

# 2. SQL Queries to Create Tables

# Customers Table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Customers (
    customer_id INTEGER PRIMARY KEY,
    name TEXT,
    city TEXT
)
''')

# Products Table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT,
    price REAL
)
''')

# Orders Table (Links Customers and Products)
cursor.execute('''
CREATE TABLE IF NOT EXISTS Orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    FOREIGN KEY(customer_id) REFERENCES Customers(customer_id),
    FOREIGN KEY(product_id) REFERENCES Products(product_id)
)
''')

# 3. Insert Dummy Data

# Adding Customers
cursor.execute("INSERT OR IGNORE INTO Customers VALUES (1, 'Ramesh', 'Hyderabad')")
cursor.execute("INSERT OR IGNORE INTO Customers VALUES (2, 'Sita', 'Vijayawada')")
cursor.execute("INSERT OR IGNORE INTO Customers VALUES (3, 'Ganesh', 'Vizag')")

# Adding Products
cursor.execute("INSERT OR IGNORE INTO Products VALUES (101, 'Laptop', 50000)")
cursor.execute("INSERT OR IGNORE INTO Products VALUES (102, 'Mouse', 500)")
cursor.execute("INSERT OR IGNORE INTO Products VALUES (103, 'Keyboard', 1000)")

# Adding Orders (Who bought what?)
cursor.execute("INSERT OR IGNORE INTO Orders VALUES (1, 1, 101, 1)") # Ramesh bought 1 Laptop
cursor.execute("INSERT OR IGNORE INTO Orders VALUES (2, 1, 102, 2)") # Ramesh bought 2 Mice
cursor.execute("INSERT OR IGNORE INTO Orders VALUES (3, 2, 103, 1)") # Sita bought 1 Keyboard
cursor.execute("INSERT OR IGNORE INTO Orders VALUES (4, 3, 101, 1)") # Ganesh bought 1 Laptop

print("--- Database Created & Data Inserted Successfully ---\n")

# 4. DATA ANALYSIS using SQL Queries

print("1. Total Sales (Revenue) Report by Product:")
# Query to calculate total money earned from each product
query1 = '''
SELECT p.product_name, SUM(o.quantity * p.price) as total_revenue
FROM Orders o
JOIN Products p ON o.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_revenue DESC;
'''
# Using Pandas to display the result neatly
df1 = pd.read_sql_query(query1, conn)
print(df1)
print("\n----------------------------")

print("2. Customer Spending Report (Who spent the most?):")
# Query to calculate total spending by each customer
query2 = '''
SELECT c.name, c.city, SUM(o.quantity * p.price) as total_spent
FROM Orders o
JOIN Customers c ON o.customer_id = c.customer_id
JOIN Products p ON o.product_id = p.product_id
GROUP BY c.name
ORDER BY total_spent DESC;
'''
df2 = pd.read_sql_query(query2, conn)
print(df2)

# Close the database connection
conn.close()