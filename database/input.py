import psycopg2


try:
    conn = psycopg2.connect("dbname='recipes' user='nstowe' host='localhost' password=''")
except:
    print("I am unable to connect to the database")


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

