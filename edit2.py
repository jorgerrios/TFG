import json
import os
import re

MACshort = ['b4:99:ba', 'cc:46:d6', 'fdwefweffea', '80:b6:86']
MACfromtext = []

file2 = open("ouis.txt", "r")

for i in range(len(MACshort)):
	file2.seek(0)
	for line in file2:
		line = line.strip()
		if re.match(MACshort[i], line):
			MACfromtext.append(line[9:])
	if len(MACfromtext) == i:
		MACfromtext.append("Not found")


print(MACfromtext)
