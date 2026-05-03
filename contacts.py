import sqlite3

# Connect to the database
conn = sqlite3.connect("contacts.db")
cursor = conn.cursor()

# Create the table with phone column added
cursor.execute("""
    CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY,
        name TEXT,
        company TEXT,
        email TEXT,
        phone TEXT
    )
""")

# Add contacts including phone numbers
cursor.execute("""
    INSERT INTO contacts (name, company, email, phone)
    VALUES (?, ?, ?, ?)
""", ("Sarah Janssen", "Faktion", "sarah@faktion.be", "+32 478 123 456"))

cursor.execute("""
    INSERT INTO contacts (name, company, email, phone)
    VALUES (?, ?, ?, ?)
""", ("Thomas Mertens", "Froomle", "thomas@froomle.com", "+32 479 234 567"))

cursor.execute("""
    INSERT INTO contacts (name, company, email, phone)
    VALUES (?, ?, ?, ?)
""", ("Lisa De Backer", "Gorilla", "lisa@gorilla.io", "+32 477 345 678"))

conn.commit()

# Read all contacts
cursor.execute("SELECT * FROM contacts")
all_contacts = cursor.fetchall()

print("All contacts:")
for contact in all_contacts:
    print(f"ID: {contact[0]} | Name: {contact[1]} | Company: {contact[2]} | Email: {contact[3]} | Phone: {contact[4]}")