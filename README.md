# Python with SQL
## Using PYODBC (open database connectivity) to connect to SQL from our Python program
### What is a Cursor and how to use it
**some functions that we can use to interact with SQL data**

- Set up pyobdc connection
- Command to install pyobdc
```pip install pyodbc```
- once installed create a python_sql.py file 
- Before you do anything please ensure you have downloaded a pyodbc driver from the link below

- https://docs.microsoft.com/en-us/sql/connect/odbc/linux-mac/install-microsoft-odbc-driver-sql-server-macos?view=sql-server-ver15

**Establish a Connection**
```python
import pyodbc

server = "databases1.spartaglobal.academy"
database = "Northwind"
username = "****"
password = "*****"
northwind_connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
```
 - server name - database name - username and password is required to connecto to pyodbc

- Verify the connection
```python
cursor = northwind_connection.cursor()
# cursor is location of you mouse/current path

cursor.execute("SELECT @@VERSION")
#select the version of current DB
row = cursor.fetchone()
print(row)


```
- Run a query in our Customer table
```python
product_rows = cursor.execute("SELECT * FROM Products").fetchall()
# Running queries in our python program to access database and table inside the DBs

for product_records in product_rows:
# iterate through the table data and find the unit prices

    print(product_records.UnitPrice)
# print(product_rows)

```
- Getting data out of our Products table
```python
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
```

Summary
- pyodbc installation and connection set up
- cursor utilsation
- fetchone() (select each record)
- fetchall() (selects all records)
- 

Task:
- Create a new file and a class with function to establish connection with pyodbc
- create a function that create a table in the DB
- create a function that prompts user to input data in that table
- create a new file called PYODBC_TASK.md and document the steps to implement the task
 
 # SQL OOP


* OOP task using pyodbc

Here we are merely creating an example of how we can create service objects related to a particular table.

## An sql manager for the products table

create an object that relates only to the products table in the Northwind database. The reason for creating a single object for any table within the database would be to ensure that all functionality we build into this relates to what could be defined as a 'business function'.

As an example the products table, although relating to the rest of the company, will service a particular area of the business in this scenario we will simply call them the 'stock' department. 

The stock department may have numerous requirements and it makes sense to contain all the requirements a code actions within a single object.

Create two files `nw_products.py` & `nw_runner.py` and then we will move into creating our object.
