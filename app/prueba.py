#   for x, y in reader:
 #      total+=x

import csv

def read_csv(path):
  with open(path,'r') as csvfile:
    reader= csv.reader(csvfile, delimiter=',')
    suma=0
    for row in reader:
      suma+=int(row[1])
    return suma
    
response = read_csv('./app/data2.csv')
print(response)