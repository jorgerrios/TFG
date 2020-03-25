import json
import os


#Obtaining differents list from the data
MAC = []
SSID = []
AuthMode = []
FirstSeen = []
Channel = []
RSSI = []
CurrentLatitude = []
CurrentLongitude = []
AltitudeMeters = []
AccuracyMeters  = []
Type = []


#Adding data to the differents array separation



with open ("data.json","r+") as file:
	data = json.load(file)

	#Collecting all the data from the JSON
	for x in range(len(data)):
		MAC.append(data[x]["MAC"])
		SSID.append(data[x]["SSID"])
		AuthMode.append(data[x]["AuthMode"])
		FirstSeen.append(data[x]["FirstSeen"])
		Channel.append(data[x]["Channel"])
		CurrentLatitude.append(data[x]["CurrentLatitude"])
		CurrentLongitude.append(data[x]["CurrentLongitude"])
		AltitudeMeters.append(data[x]["AltitudeMeters"])
		AccuracyMeters.append(data[x]["AccuracyMeters"])
		Type.append(data[x]["Type"])



	for x in range(len(data)):
		if Channel[x] <= 11:
			data[x].update({"Frecuency used": "2,5GHz"})
		else:
			data[x].update({"Frecuency used": "5GHz"})






		#data[0].update({"color": "white"})


	print(data)