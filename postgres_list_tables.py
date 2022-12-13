# Import the necessary modules
import psycopg2

import os
from dotenv import load_dotenv
load_dotenv()


# Set the database connection parameters
DB_HOST = os.getenv('DATABASE_HOST')
DB_NAME = os.getenv('DATABASE_NAME')
DB_USER = os.getenv('DATABASE_USERNAME')
DB_PASS = os.getenv('DATABASE_PASSWORD')


# Connect to the database
conn = psycopg2.connect(user=DB_USER, password=DB_PASS, database=DB_NAME, host=DB_HOST)

# Create a cursor object
cur = conn.cursor()

# Execute a query to get the list of tables
cur.execute('SELECT table_name FROM information_schema.tables WHERE table_schema = \'public\';')

# Print the list of tables
print('Tables in the database:')
for table in cur.fetchall():
    print(table[0])

# Close the cursor and connection
cur.close()
conn.close()