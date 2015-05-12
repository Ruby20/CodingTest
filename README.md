# CodingTest

Write a program that will process a CSV file of courses as well as a CSV file of students.
You will need to determine the type of data in the CSV file based on the headers in the first row. 
Your program will output a list of active courses, and for each course, a list of active students enrolled in that course.

The repo contains three files
dbConnection - functions to get database connection and execute queries
csvReader - use a csv dict reader to read the csv files
Main - Insert student and course data into the database and process queries to get the active list of students and courses.


#TODO
 Regexp parse and check for special characters in csv files  
 testcaseFile empty
 Database columns missing
 read the column type to determine the type of data (partially implemented a function)
 Some of the test cases to think about - Perform sanity checks on data, handle database exceptions, test with large csv files. Course_id and u_id mismatch.
 
