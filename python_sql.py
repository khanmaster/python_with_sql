# This lesson will include connection to our SQL DB from Python using PYODBC

# pyodbc driver from microsoft helps us to connect to SQL instance
# we will connect to our Northwind DB which you have already used in SQL week

# Before you do anything please ensure you have downloaded a pyodbc driver

import pyodbc

server = "databases1.spartaglobal.academy"
database = "Northwind"
username = "***"
password = "*******"
northwind_connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
# server name - database name - username and password is required to connecto to pyodbc

cursor = northwind_connection.cursor()
# cursor is location of you mouse/current path

cursor.execute("SELECT @@VERSION")
#select the version of current DB
row = cursor.fetchone()
print(row)
#
# #In our DB we have table called Customers that has customers data available
# cust_row = cursor.execute("SELECT * FROM Customers;").fetchall()
# # using fetchall() method we can get all the data available inside our Customer's table
# for records in cust_row:
#    print(records)
#
# # We have another table in the DB called Products

product_rows = cursor.execute("SELECT * FROM Products").fetchall()
# Running queries in our python program to access database and table inside the DBs

for product_records in product_rows:
# iterate through the table data and find the unit prices

    print(product_records.UnitPrice)
# print(product_rows)

product_row = cursor.execute("SELECT * FROM Products")
# getting the Product table data

# Iterating through the data until the last line of the data (until condition is False)

# Combination of our loop and control flow to ensure we only iterate through the data as long as the data is available

while True:
    records = product_row.fetchone()
    if records is None:
        # when there are no records left (value is None) stop
        break
    print(records.UnitPrice)