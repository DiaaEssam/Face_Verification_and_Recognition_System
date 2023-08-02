import sqlite3
import os

current_directory = os.path.abspath(os.path.dirname(__file__))
database_path = os.path.join(current_directory, "Institution.db")
if os.path.exists(database_path):
        # Delete the file
        os.remove(database_path)
# Connect to the SQLite database
conn = sqlite3.connect(database_path)

# Create a cursor object
c = conn.cursor()

# Define the SQL query to create the table
query = 'CREATE TABLE Person (id INTEGER PRIMARY KEY, name TEXT, encoding FLOAT)'

# Execute the query
c.execute(query)

# Commit the changes
conn.commit()

# Close the cursor and connection
c.close()
conn.close()