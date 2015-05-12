import dbConnection as db 
from csvReader import csv_reader
from csvReader import csvs

#Read csv and an initial working code

filename = 'student.csv'
fi = 'course.csv'
#alist =  csv_reader(filename)
dlist = csvs(filename)
two_list = csvs(fi)

#print dlist
#get the db connection handler
conn = sqlite3.connect(':memory:', isolation_level=None)
cur = conn.cursor()
con = db.db_connect()
#query1 = 'INSERT INTO student1 (Course_id,user_name,state,user_id)  VALUES ("C628944","Noah Thomas","active","U531649")'
#print query1
#con.cursor().execute(query1)
