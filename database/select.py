# Install postgres databse
# pip install psycopg2-binary


# Example using the psql program
# insert into recipes (name, url, source) values ('Deep Fried Spaghetti ', 'www.foodnetwork.com/id=5431233', 'Food Network');

# recipes=# select * from recipes;
# id |         name          |              url               |    source    | created-at
# ----+-----------------------+--------------------------------+--------------+------------
#  1 | tacos supreme         | www.tacos.com/id=4234234       | Taco Recipe  |
#  2 | Deep Fried Spaghetti  | www.foodnetwork.com/id=5431233 | Food Network |


import psycopg2


try:
    conn = psycopg2.connect("dbname='recipes' user='nstowe' host='localhost' password=''")
except:
    print("I am unable to connect to the database")

cur = conn.cursor()

cur.execute("""select * from recipes""")

rows = cur.fetchall()

print("\nShow me the data:\n")

for row in rows:
    print("   ", row[1], "\t\t\t", row[2])
