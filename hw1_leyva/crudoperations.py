import mysql.connector
from mysql.connector import Error

import creds

from sql import create_con
from sql import execute_myquery
from sql import execute_read_myquery

#connection to database
mycreds = creds.creds()

con = create_con(mycreds.hostname, mycreds.username, mycreds.password, mycreds.database)

#CRUD operations - Create, Read, Update, Delete

#create a new entry in DB

#create a new table
# sql = "create table sales(id int(2), seller varchar(20), product varchar(20), quantity int(3), price float(2))"
# execute_myquery(con, sql)

#sql = "insert into users(firstname, lastname, email) values('myclass', 'lastnameclass', 'myclass@uh.edu')"
#execute_myquery(con, sql)

#update row information in table
# uid =  5
# sql =  "update users set email='mycode@uh.edu' where id=%s" % (uid)
# execute_myquery(con, sql)

#delete a row from DB
#uid = 4
#sql = "delete from users where id=%s" % (uid)
#execute_myquery(con, sql)

#read rows form DB
sql = "select * from sales"
tablerows = execute_read_myquery(con, sql)
print(tablerows)
