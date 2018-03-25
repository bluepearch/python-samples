# Install postgres databse
# pip install psycopg2-binary

# Example using the psql program
# insert into recipes (name, url, source) values ('Deep Fried Spaghetti ', 'www.foodnetwork.com/id=5431233', 'Food Network');

import psycopg2

conn = psycopg2.connect("dbname='recipes' user='nstowe' host='localhost' password=''")

print ("Lets add a recipe!")

name = input("Enter name: ")
url = input ("Enter URL: ")
source = input ("Enter name of source: ")



cur = conn.cursor()  # open a cursor to database

cur.execute("insert into recipes (name, url, source) values ('%s', '%s', '%s')" % (name, url, source) )

conn.commit()  # have to commit the transaction

cur.execute("select * from recipes")

rows = cur.fetchall()

cur.close()



print("\nShow me the data:\n")

for row in rows:
    print("\t", row[1], "\t\t", row[2])

