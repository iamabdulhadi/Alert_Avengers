
import unittest
import sqlite3
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database import init_db

class TestDatabase(unittest.TestCase):
    
    def setUp(self):
        self.test_db = 'test_banking.db'
        if os.path.exists(self.test_db):
            os.remove(self.test_db)
    
    def tearDown(self):
        if os.path.exists(self.test_db):
            os.remove(self.test_db)
    
    def test_database_initialization(self):
        """Test that the database is initialized correctly"""
        # Create a test database
        conn = sqlite3.connect(self.test_db)
        cursor = conn.cursor()
        
        # Create tables (copy from init_db function)
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
        
        conn.commit()
        
        # Check that tables exist
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        table_names = [table[0] for table in tables]
        
        self.assertIn('customers', table_names)
        self.assertIn('accounts', table_names)
        self.assertIn('transactions', table_names)
        self.assertIn('branches', table_names)
        
        conn.close()
    
    def test_sample_data_insertion(self):
        """Test that sample data is inserted correctly"""
        conn = sqlite3.connect(self.test_db)
        cursor = conn.cursor()
        
        # Create tables and insert sample data
        cursor.execute('''
            CREATE TABLE customers (
                customer_id INTEGER PRIMARY KEY,
                first_name TEXT,
                last_name TEXT,
                address TEXT
            )
        ''')
        
        cursor.execute("INSERT INTO customers (customer_id, first_name, last_name, address) VALUES (1, 'John', 'Doe', '123 Main St')")
        cursor.execute("INSERT INTO customers (customer_id, first_name, last_name, address) VALUES (2, 'Jane', 'Smith', '456 Oak Ave')")
        
        conn.commit()
        
        # Check that data was inserted
        cursor.execute("SELECT COUNT(*) FROM customers")
        count = cursor.fetchone()[0]
        self.assertEqual(count, 2)
        
        cursor.execute("SELECT first_name, last_name FROM customers WHERE customer_id = 1")
        customer = cursor.fetchone()
        self.assertEqual(customer[0], 'John')
        self.assertEqual(customer[1], 'Doe')
        
        conn.close()

if __name__ == '__main__':
    unittest.main()

