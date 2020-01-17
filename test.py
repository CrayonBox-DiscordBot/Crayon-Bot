#  Copyright (c) 2020.
#  All rights lies to "VukAnd12#4407" and "Gravity Assist#0852"
import pymysql
import crayon

print(crayon.DB.execute_query("SELECT * From server;"))
"""
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='',
                     db='crayon')

cursor = db.cursor()
cursor.execute('SELECT * From server;')

rows = cursor.fetchall()

for row in rows:
    print("{0} {1}".format(row[0], row[1]))"""
