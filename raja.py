import mysql.connector
con=mysql.connector.connect(user="root",host="localhost",port="3306",database="sigma")

if con:
    print("connect")
else:
    print("not  connect")