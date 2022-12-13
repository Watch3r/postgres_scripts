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
conn = psycopg2.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASS)

# Print a message if the connection is successful
if conn:
    print("Successfully connected to the database!")
