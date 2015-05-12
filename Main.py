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

for row in dlist:
    #print row["user_id"]
    keys = row.keys()
    values = row.values()
    #print values
    columns = ', '.join(keys)                  # TODO Check the order
    placeholder = "'{0}','{1}','{2}','{3}'".format(row[keys[0]],values[1],values[2],values[3])

 
#TODO batch process the query result
    query = "INSERT INTO student1 ('course_id','user_name','state','user_id') VALUES (%s);" % (placeholder)
    #print query
#==============================================================================
#     try:
#        con.cursor().executemany(query, values) 
#        con.commit()
#     except:
#==============================================================================
    db.execute_query(con,query)    
    con.commit() 
    result = con.cursor().execute("SELECT * FROM student1;") 
#print result.fetchall() 
    
for row in two_list:
    keys = row.keys()
    values = row.values()
    #print values
    columns = ', '.join(keys)
    placeholder = "'{0}','{1}','{2}'".format(values[0],values[1],values[2])
    #TODO batch process the query result
    query = "INSERT INTO course ('course_id','state','course_name') VALUES (%s);" % (placeholder)
    con.cursor().execute(query)    
    con.commit() 
    result1 = con.cursor().execute("SELECT * FROM course;") 
#print result1.fetchall()     
    
res1 = con.cursor().execute("SELECT course_id from course WHERE state is 'active';").fetchall()    
print res1

result_list = []

#Then need to filter the list of active courses with active students 
for c_id in res1:
  #Course = str(c_id[0])
  Course =  c_id[0]
  
  query = "SELECT user_name,course_id from student1 WHERE state = 'active' AND course_id='{0}';".format(Course)
  #print query  
  res2= con.cursor().execute(query).fetchall()    
  result_list.append(res2) 

print result_list 
with open('test.txt', 'w') as f:
    for row in result_list:
        #print row
        f.write("%s\n" % str(row))














