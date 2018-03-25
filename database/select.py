# Install postgres databse
# pip install psycopg2-binary



# recipes=# select * from recipes;
# id |         name          |              url               |    source    | created-at
# ----+-----------------------+--------------------------------+--------------+------------
#  1 | tacos supreme         | www.tacos.com/id=4234234       | Taco Recipe  |
#  2 | Deep Fried Spaghetti  | www.foodnetwork.com/id=5431233 | Food Network |


import psycopg2


conn = psycopg2.connect("dbname='recipes' user='nstowe' host='localhost' password=''")

cur = conn.cursor()

cur.execute("""select * from recipes""")

rows = cur.fetchall()

print("\nShow me the data:\n")

for row in rows:
    print("   ", row[1], "\t\t\t", row[2])
