import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('expenses.db')
c = conn.cursor()

# Create 'users' table
c.execute('''
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        password TEXT
    )
''')

# Create 'expenses' table
c.execute('''
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        amount REAL,
        category TEXT,
        date TEXT,
        note TEXT
    )
''')

# Create 'income' table
c.execute('''
    CREATE TABLE IF NOT EXISTS income (
        username TEXT,
        month TEXT,
        amount REAL,
        PRIMARY KEY(username, month)
    )
''')

# Create 'savings_goal' table
c.execute('''
    CREATE TABLE IF NOT EXISTS savings_goal (
        username TEXT PRIMARY KEY,
        goal_amount REAL,
        deadline TEXT
    )
''')

# Commit changes and close connection
conn.commit()
conn.close()

print("✅ Database initialized successfully!")
