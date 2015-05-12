import sqlite3


def db_connect():
#conn = sqlite3.connect('course.db')
    #store the sqlite db in memory RAM
    conn = sqlite3.connect(':memory:', isolation_level=None)
    cur = conn.cursor()
    # create table "student" and "course",relation is "Many-to-One"
    
        
    cur.execute('''CREATE TABLE IF NOT EXISTS course
                    (course_id INTEGER PRIMARY KEY NOT NULL,
                     course_name TEXT, 
                     state TEXT)''')
    cur.execute('''CREATE TABLE IF NOT EXISTS student1
                    (course_id INTEGER,
                     user_name TEXT,
                     state TEXT, 
                     user_id TEXT PRIMARY KEY  NOT NULL,
                     FOREIGN KEY(course_id) REFERENCES course(course_id))''')
     
    return conn


def execute_query(conn,query):
    cur = conn.cursor()
    res = cur.execute(query).fetchall()
    conn.commit()
    return res
          
