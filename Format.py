import json
import os
import re
import requests

f= open("p.json","w+")
f.close()


CurrentLatitude = []
CurrentLongitude = []



with open("dataOutput.json", "r+") as file:
	data = json.load(file)
	for x in range(len(data)):
		CurrentLatitude.append(data[x]["CurrentLatitude"])
		CurrentLongitude.append(data[x]["CurrentLongitude"])
	for element in data:
		element.pop('CurrentLatitude', None)
		element.pop('CurrentLongitude', None)
	for x in range(len(data)):
		data[x].update({"Location": {"lat": CurrentLatitude[x], "lon": CurrentLongitude[x]}})
	for x in range(len(data)):
		f= open("p.json","a+")
		f.write('{"index":{"_id":"' + str(x+1) + '"}}' + "\n")
		f.write(json.dumps(data[x]) + "\n")
		f.close()
