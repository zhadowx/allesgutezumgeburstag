import mysql.connector

dbconfig = { 'host': '127.0.0.1',
             'user': 'lsearch',
             'password': '1234567',
             'database': 'lsearchlogDB', }

conn = mysql.connector.connect(**dbconfig)
cursor = conn.cursor()

_SQL = """insert into log
             (phrase, letters, ip, browser_string, results)
             values
             (%s, %s, %s, %s, %s)"""

cursor.execute(_SQL, ('palomo', 'o', '127.0.0.1', 'Chrome', "{'o'}"))
conn.commit()

_SQL = """select * from log"""
cursor.execute(_SQL)
for row in cursor.fetchall():
  print(row)
