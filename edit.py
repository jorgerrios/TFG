import csv
import os
import sys

#Python that delete the first row in the csv, information about the APP
orden = str(sys.argv[1])

lines = list()
keyWord1 = 'brand=' + orden
with open('WigleCSV2.csv', 'r') as readFile:
	reader = csv.reader(readFile)
	for row in reader:
		lines.append(row)
		for field in row:
			if field == keyWord1:
				lines.remove(row)

with open('mycsv.csv', 'w') as writeFile:
	writer = csv.writer(writeFile)
	writer.writerows(lines)


#Deleting all the information that make the execution time slow, leaving only WIFI

lines = list()
keyWord2 = 'GSM'
keyWord3 = 'BLE'
with open('mycsv.csv', 'r') as readFile:
	reader = csv.reader(readFile)
	for row in reader:
		lines.append(row)
		for field in row:
			if field == keyWord2 or field == keyWord3:
				lines.remove(row)

with open('mycsv.csv', 'w') as writeFile:
	writer = csv.writer(writeFile)
	writer.writerows(lines)