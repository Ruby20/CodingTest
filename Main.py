import dbConnection as db 
from csvReader import csvs 


#Read csv and an initial working code
student_file = 'student.csv'
course_file = 'course.csv'


student_list = csvs(student_file)
course_list = csvs(course_file)

#print student_list.fieldnames


#get the db connection handler
con = db.db_connect()

#=========================================================================================
#inserting the student data to the db
for row in student_list:
    #print row["user_id"]
    keys = row.keys()
    #To get the datatype of the field
    Dtype =get_datatype(keys[0])
    values = row.values()
    #print values
    
    columns = ', '.join(keys)
    print columns
    # TODO Check the order                 
    placeholder = "'{0}','{1}','{2}','{3}'".format(row[keys[0]],row[keys[1]],row[keys[2]],row[keys[3]])
    
    #TODO batch process the query result
    query = "INSERT INTO student1 ('user_id','user_name','state','course_id') VALUES (%s);" % (placeholder)
    print query
    db.execute_query(con,query)    
    
    result = con.cursor().execute("SELECT * FROM student1;") 
print result.fetchall() 
#==========================================================================================

#=======================================================================================
#inserting the course data to the db    
for row in course_list:
    keys = row.keys()
    values = row.values()
    #print values
    columns = ', '.join(keys)
    placeholder = "'{0}','{1}','{2}'".format(row[keys[0]],row[keys[1]],row[keys[2]])
    #TODO batch process the query result
    query = "INSERT INTO course ('course_id','state','course_name') VALUES (%s);" % (placeholder)
    db.execute_query(con,query)    
#result1 = con.cursor().execute("SELECT * FROM course;") 
#print result1.fetchall()     
#========================================================================================

#get the list of active courses  
query_course = "SELECT course_id from course WHERE state is 'active';"  
active_courses = db.execute_query(con,query_course)    
print active_courses


#create a list to store results 
result_list = []
#Then need to filter the list of active courses with active students 
for c_id in active_courses:
  #Course = str(c_id[0])
  course_id =  c_id[0]
  query_student = "SELECT user_name,course_id from student1 WHERE state = 'active' AND course_id='{0}';".format(course_id)
  #print query  
  active_students= db.execute_query(con,query_student)   
  result_list.append(active_students) 
print result_list 

#TODO format the output
with open('test.txt', 'w') as f:
    f.write("'userName'   'courseID'\n")
    for row in result_list:
        #print row
        f.write("%s\n" % str(row))














