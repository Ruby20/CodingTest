import csv


def csv_reader(filename):
    mycsv = open(filename, 'rb')
    with open(filename, 'rb') as f:
        #To get the null value error in csv file
        reader = csv.reader(f.replace('\0','')for f in mycsv )
        your_list = list(reader)
        
    for item in your_list:
        
        #print item
        str1 = " ".join(item)
        str2 = str1.split(",")
        #TODO Check order and course_id
    return str2
