import csv
import os
import sys

#Python that delete the first row in the csv, information about the APP
#Deleting everything that is unused
brand = raw_input("Enter your mobile phone brand : ") 


lines = list()
keyWord1 = 'brand=' + brand
keyWord2 = 'GSM'
keyWord3 = 'BLE'
keyWord4 = 'BT'
with open('WIGLE.csv', 'r') as readFile:
	reader = csv.reader(readFile)
	for row in reader:
		lines.append(row)
		for field in row:
			if field == keyWord1 or field == keyWord2 or field == keyWord3 or field == keyWord4:
				lines.remove(row)

with open('mycsv.csv', 'w') as writeFile:
	writer = csv.writer(writeFile)
	writer.writerows(lines)

