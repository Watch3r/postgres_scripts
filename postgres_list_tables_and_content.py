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

# Create a cursor
cur = conn.cursor()

# Execute a query to get the list of tables
cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public'")

# Save results to variable
results = cur.fetchall()

# Print the list of tables
print("Tables in database:")
for table in results:
    print(f"- {table[0]}")

# Loop through the tables and print their contents
for table in results:
    print("-"*50)

    table_name = table[0]
    print(f"Table: {table_name}")
    cur.execute(f'SELECT column_name, data_type, character_maximum_length FROM information_schema.columns WHERE table_name = \'{table_name}\';')

    schema_column_names = tuple([column[0] for column in cur.fetchall()])
    print(f"Schema: {schema_column_names}")

    cur.execute(f"SELECT * FROM {table_name}")
    print(f"Content: ")

    for row in cur.fetchall():
        print(row)

# Close the cursor and connection
cur.close()
conn.close()
