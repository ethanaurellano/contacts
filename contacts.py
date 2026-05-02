import sqlite3

# Connect to the database
# This creates a file called contacts.db automatically
conn = sqlite3.connect("contacts.db")
cursor = conn.cursor()

# Create the contacts table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY,
        name TEXT,
        company TEXT,
        email TEXT
    )
""")

conn.commit()
print("Database and table created successfully")