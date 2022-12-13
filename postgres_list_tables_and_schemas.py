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

# Print the list of tables and their schemas
print('Tables in the database:')
for table in cur.fetchall():
    table_name = table[0]
    print(f'\nTable: {table_name}')

    # Execute a query to get the schema for the table
    cur.execute(f'SELECT column_name, data_type, character_maximum_length FROM information_schema.columns WHERE table_name = \'{table_name}\';')

    # Print the table schema
    print('Column name    Data type    Maximum length')
    for column in cur.fetchall():
        column_name = column[0]
        data_type = column[1]
        max_length = column[2]
        print(f'{column_name}    {data_type}    {max_length}')

