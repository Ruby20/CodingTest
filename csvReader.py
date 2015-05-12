'''Code to read the csv files using dict reader csv module
'''
import csv
import re

def csv_reader(filename):
    mycsv = open(filename, 'rb')
    with open(filename, 'rb') as f:
        #To get rid of the null value error in csv file utf-16
        try:
           reader = csv.reader(f.replace('\0','')for f in mycsv )
        except csv.Error,e:
           sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e)) 
        a_list = list(reader)
        
    for item in your_list:
        #print item
        str1 = " ".join(item)
        str2 = str1.split(",")
        #TODO Check order and course_id
    return str2


#def sanitize(alist):     
def csvs(filename):
    mycsv = open(filename, 'rb')
    try:
       input_file = csv.DictReader(open(filename),dialect='excel' )
    except csv.Error, e:
       sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))
    #TODO Regexp parse and check for special characters   
    #TODO testcaseFile empty
    #Database columns missing
        
    return input_file

#TODO read the column type  
def get_datatype(key):
    start = '('
    end = ')'
    data_type = key[key.find(start)+1: key.find(end)]    
    return  data_type
    
    
