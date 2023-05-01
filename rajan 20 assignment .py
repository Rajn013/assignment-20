#!/usr/bin/env python
# coding: utf-8

# Set the variable test1 to the string 'This is a test of the emergency text system,' and save test1 to a file named test.txt.
#         

# In[9]:


test1 = 'this is a test of the emergency text system'
with open('test.txt','w')as file:
    file.write(test1)


# 2. Read the contents of the file test.txt into the variable test2. Is there a difference between test 1 and test 2?

# In[10]:


test1 = 'this is a test of the emergency text system'
with open('test.txt','w')as file:
    file.write(test1)


# Create a CSV file called books.csv by using these lines:
# title,author,year
# The Weirdstone of Brisingamen,Alan Garner,1960
# Perdido Street Station,China Miéville,2000
# Thud!,Terry Pratchett,2005
# The Spellman Files,Lisa Lutz,2007
# Small Gods,Terry Pratchett,1992
# 

# In[11]:


import csv

data = [
    ['title', 'author', 'year'],
    ['The Weirdstone of Brisingamen', 'Alan Garner', 1960],
    ['Perdido Street Station', 'China Miéville', 2000],
    ['Thud!', 'Terry Pratchett', 2005],
    ['The Spellman Files', 'Lisa Lutz', 2007],
    ['Small Gods', 'Terry Pratchett', 1992]
]


with open('books.csv', 'w', newline='') as file:

    
    writer = csv.writer(file)

    
    for row in data:
        writer.writerow(row)


# Use the sqlite3 module to create a SQLite database called books.db, and a table called books with these fields: title (text), author (text), and year (integer).

# In[27]:


import sqlite3

# Create a connection to the database
conn = sqlite3.connect('books.db')

# Create a cursor object to execute SQL statements
cursor = conn.cursor()

# Check if the 'genre' column exists
cursor.execute("PRAGMA table_info(books)")
columns = [column[1] for column in cursor.fetchall()]

if 'genre' not in columns:
    # Define a SQL statement to add a new column to the 'books' table
    alter_table_sql = '''
        ALTER TABLE books
        ADD COLUMN genre TEXT
    '''

    # Execute the SQL statement to modify the table
    cursor.execute(alter_table_sql)

# Commit the changes and close the connection
conn.commit()
conn.close()


#  Read books.csv and insert its data into the book table

# In[28]:


import csv
import sqlite3

# Create a connection to the database
conn = sqlite3.connect('books.db')

# Create a cursor object to execute SQL statements
cursor = conn.cursor()

# Open the CSV file
with open('books.csv', 'r') as file:

    # Create a CSV reader object
    reader = csv.reader(file)

    # Skip the header row
    next(reader)

    # Loop over the rows in the CSV file
    for row in reader:

        # Extract the data from the row
        title = row[0]
        author = row[1]
        year = int(row[2])

        # Define a SQL statement to insert the data into the 'books' table
        insert_sql = '''
            INSERT INTO books (title, author, year)
            VALUES (?, ?, ?)
        '''

        # Execute the SQL statement to insert the data
        cursor.execute(insert_sql, (title, author, year))

# Commit the changes and close the connection
conn.commit()
conn.close()


# Select and print the title column from the book table in alphabetical order.

# In[29]:


import sqlite3

# Create a connection to the database
conn = sqlite3.connect('books.db')

# Create a cursor object to execute SQL statements
cursor = conn.cursor()

# Define a SQL statement to select the 'title' column from the 'books' table
select_sql = '''
    SELECT title
    FROM books
    ORDER BY title ASC
'''

# Execute the SQL statement to select the data
cursor.execute(select_sql)

# Fetch all the rows returned by the SELECT statement
rows = cursor.fetchall()

# Print the 'title' column of each row
for row in rows:
    print(row[0])

# Close the connection
conn.close()


# 7. from the book table, select and print all columns in the order of publication.

# In[30]:


import sqlite3


conn = sqlite3.connect('books.db')


cursor = conn.cursor()

select_sql = '''
    SELECT *
    FROM books
    ORDER BY year ASC
'''


cursor.execute(select_sql)


rows = cursor.fetchall()


for row in rows:
    print(row)


conn.close()


# 8.Use the sqlalchemy module to connect to the sqlite3 database books.db that you just made in
# exercise 6.

# In[31]:


import sqlalchemy as db

engine = db.create_engine('sqlite:///books.db')

connection = engine.connect()

query = db.select([db.text('*')]).select_from(db.text('books'))
result_proxy = connection.execute(query)
results = result_proxy.fetchall()

for row in results:
    print(row)

connection.close()


# Install the Redis server and the Python redis library (pip install redis) on your computer. Create a
# Redis hash called test with the fields count (1) and name (&#39;Fester Bestertester&#39;). Print all the fields for
# test.

# In[7]:


get_ipython().system('pip install redis')


# In[ ]:


import redis

r = redis.Redis(host='localhost', port=6379)

r.hset("test", "count", 1)
r.hset("test", "name", "Fester Bestertester")

print(r.hgetall("test"))


# 10.Increment the count field of test and print it.

# In[ ]:


import redis

r = redis.Redis(host='localhost', port=6379)

r.hincrby("test", "count", 1)


print(r.hget("test", "count"))

