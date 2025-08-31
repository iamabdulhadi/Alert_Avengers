
import sqlite3

def init_db():
    conn = sqlite3.connect('banking.db')
    cursor = conn.cursor()

    # Create tables
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            customer_id INTEGER PRIMARY KEY,
            first_name TEXT,
            last_name TEXT,
            address TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS accounts (
            account_id INTEGER PRIMARY KEY,
            customer_id INTEGER,
            account_type TEXT,
            balance REAL,
            FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            transaction_id INTEGER PRIMARY KEY,
            account_id INTEGER,
            transaction_type TEXT,
            amount REAL,
            transaction_date TEXT,
            FOREIGN KEY (account_id) REFERENCES accounts(account_id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS branches (
            branch_id INTEGER PRIMARY KEY,
            branch_name TEXT,
            location TEXT
        )
    ''')

    # Insert sample data
    cursor.execute("INSERT OR IGNORE INTO customers (customer_id, first_name, last_name, address) VALUES (1, 'John', 'Doe', '123 Main St')")
    cursor.execute("INSERT OR IGNORE INTO customers (customer_id, first_name, last_name, address) VALUES (2, 'Jane', 'Smith', '456 Oak Ave')")

    cursor.execute("INSERT OR IGNORE INTO accounts (account_id, customer_id, account_type, balance) VALUES (101, 1, 'Savings', 5000.00)")
    cursor.execute("INSERT OR IGNORE INTO accounts (account_id, customer_id, account_type, balance) VALUES (102, 1, 'Checking', 2500.00)")
    cursor.execute("INSERT OR IGNORE INTO accounts (account_id, customer_id, account_type, balance) VALUES (201, 2, 'Savings', 10000.00)")

    cursor.execute("INSERT OR IGNORE INTO transactions (transaction_id, account_id, transaction_type, amount, transaction_date) VALUES (1001, 101, 'Deposit', 1000.00, '2023-01-05')")
    cursor.execute("INSERT OR IGNORE INTO transactions (transaction_id, account_id, transaction_type, amount, transaction_date) VALUES (1002, 102, 'Withdrawal', 200.00, '2023-01-06')")
    cursor.execute("INSERT OR IGNORE INTO transactions (transaction_id, account_id, transaction_type, amount, transaction_date) VALUES (1003, 201, 'Deposit', 500.00, '2023-01-07')")

    cursor.execute("INSERT OR IGNORE INTO branches (branch_id, branch_name, location) VALUES (1, 'Downtown Branch', 'New York')")
    cursor.execute("INSERT OR IGNORE INTO branches (branch_id, branch_name, location) VALUES (2, 'Uptown Branch', 'New York')")

    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
    print("Database 'banking.db' initialized with sample data.")

