import sqlite3
import string
import random
# Connect to the database
conn = sqlite3.connect('mailpas.db')

#generates username and password
def generate_username(length):
    # Choose a random combination of letters and digits
    letters_and_digits = string.ascii_letters + string.digits
    # Use random.sample to choose a random sequence of characters
    return ''.join(random.sample(letters_and_digits, length))

# Create a table to store passwords and emails
conn.execute('''CREATE TABLE passwords (email text, password text)''')

# Generate a random username with 8 characters
for i in range(2000):
    # Define the email and password as variables
    USERNAME = generate_username(8)+ "@gmail.com"
    PASSWORD = generate_username(8)
    conn.execute('''INSERT INTO passwords VALUES (?, ?)''', (USERNAME, PASSWORD))
    # Insert the data into the table using the variables

# Commit the changes to the database
conn.commit()

# Close the connection to the database
conn.close()
