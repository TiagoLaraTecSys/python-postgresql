'''
Created on 10 de jul de 2020

@author: larat
'''
from psycopg2._psycopg import cursor

print('Hello Postgre')
import psycopg2

#Connect to the db
con = psycopg2.connect(
    host = "localhost",
    database = "test",
    user = "postgres",
    password = "1s1@f23ty"
)

#Cursor
cur = con.cursor()

#execute query
cur.execute("select * from mainTable")


rows = cur.fetchall()

for r in rows:
    print(f"capsule {r[0]} post {r[1]}")

#close the connection
con.close()




