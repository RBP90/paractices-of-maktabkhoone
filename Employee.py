import mysql.connector
import os

password = os.environ.get('MYSQL_PASSWORD')
cnx = mysql.connector.connect(user='root', password=password,
                              host='127.0.0.1',
                              database='maktabkhoone')

cursor = cnx.cursor()

query = 'SELECT * FROM employee ORDER BY Height DESC, Weight ASC;'
cursor.execute(query)

for (Name , Height , Weight) in cursor:
    print(Name , Height , Weight)


cnx.close()
