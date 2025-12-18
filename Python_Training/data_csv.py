import csv

mypath = (r" C:\\Users\\User\\PycharmProjects\\pythonProject3\\servershealth.csv ")
with open(mypath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        print(row)

