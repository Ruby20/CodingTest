import sqlite3


def db_connect():
#conn = sqlite3.connect('school.db')
    conn = sqlite3.connect(':memory:', isolation_level=None)
    cur = conn.cursor()
    # create table "student" and "course". The relation is "Many-to-One"
    # The order of csv files do matter since we have the foreign key constrain on course_id
    cur.execute('''CREATE TABLE IF NOT EXISTS course
                    (course_id INTEGER PRIMARY KEY NOT NULL,
                     course_name TEXT, 
                     state TEXT)''')
    cur.execute('''CREATE TABLE student1
                    (course_id INTEGER,
                     user_name TEXT,
                     state TEXT, 
                     user_id TEXT PRIMARY KEY  NOT NULL,
                     FOREIGN KEY(course_id) REFERENCES course(course_id))''')
     
    return conn

