import csv     # imports the csv module
import json

csv_file = open('C:\\Users\\Sam\\Downloads\\SalesJan2009.csv')
read_csv = csv.reader(csv_file)
csv_data = list(read_csv)

print(csv_data)


with open('csv_data', 'w') as outfile:
    json.dump(csv_data, outfile)

print(outfile)
