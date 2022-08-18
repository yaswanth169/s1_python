import csv

with open('C:\Users\yaswa\Desktop\PFSD\country.csv') as f:
    csv_reader = csv.reader(f)
    for line in csv_reader:
        print(line)
