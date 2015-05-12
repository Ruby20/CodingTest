import dbConnection
import unittest

#Unit testing the function
connection = db.db_connect()
query = ("INSERT INTO student1('user_id','user_name','state','course_id') VALUES ('None','Alexander Reed','active','1')")
second_query = ("INSERT INTO student1('user_id','user_name','state','course_id') VALUES ('None','Alexander Reed','active','1')")
db.execute_query(connection,query)
db.execute_query(connection,second_query)
select = ("SELECT * FROM student1")

assert (db.execute_query(connection,select)),'UNIQUE constraint failed: student1.user_id'
