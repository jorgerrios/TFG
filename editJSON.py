import json
import os
import re


# Obtaining differents list from the data
MAC = []
MACshort = []
MACfromtext = []
SSID = []
AuthMode = []
FirstSeen = []
Channel = []
RSSI = []
CurrentLatitude = []
CurrentLongitude = []
AltitudeMeters = []
AccuracyMeters = []
Type = []
FinalCompany = []
Routers = []
Companies = ["MOVISTAR","WLAN","ORANGE","FTE","FLYBOX","MIFIBRA","LIVEBOX","JAZZTEL","VODAFONE","ONO","LOWI","MIWIFI","MASMOVIL","MAS-MOVIL"]
Company = ["MOVISTAR","MOVISTAR","ORANGE/JAZZTEL","ORANGE/JAZZTEL","ORANGE/JAZZTEL","ORANGE/JAZZTEL","ORANGE/JAZZTEL","ORANGE/JAZZTEL","VODAFONE","VODAFONE","LOWI","MASMOVIL","MASMOVIL","MASMOVIL"]

# Adding data to the differents array separation
# Opening diferents txt neededs

file2 = open("ouis2.txt", "r")
file3 = open("companies.txt", "r")
file4 = open("routers.txt","r")


# Open the file like a dictionary
with open("dataLONG.json", "r+") as file:
	data = json.load(file)

	# Collecting all the data from the JSON
	for x in range(len(data)):
		MAC.append(data[x]["MAC"])
		if data[x]["SSID"] == '':
			SSID.append("Without SSID")
		else:
			SSID.append(data[x]["SSID"])
		AuthMode.append(data[x]["AuthMode"])
		FirstSeen.append(data[x]["FirstSeen"])
		Channel.append(data[x]["Channel"])
		CurrentLatitude.append(data[x]["CurrentLatitude"])
		CurrentLongitude.append(data[x]["CurrentLongitude"])
		AltitudeMeters.append(data[x]["AltitudeMeters"])
		AccuracyMeters.append(data[x]["AccuracyMeters"])
		Type.append(data[x]["Type"])

	# Adding the transmission channel value
	for x in range(len(data)):
		if Channel[x] <= 11:
			data[x].update({"Frecuency used": "2,5GHz"})
		else:
			data[x].update({"Frecuency used": "5GHz"})

	# Adding the fabricant name to the JSON
	# Making the MAC address short
	for mac in range(len(MAC)):
		MACshort.append(MAC[mac][:8])

	# Searching it in documments
	for i in range(len(MACshort)):
		string = MACshort[i][:2].upper() + '-' + MACshort[i][3:5].upper() + '-' + MACshort[i][6:8].upper()
		for line in file2:
			line = line.strip()
			if re.match(string, line):
				MACfromtext.append(line[18:])
		if len(MACfromtext) == i:
			MACfromtext.append("Not found")
		file2.seek(0)

	for x in range(len(data)):
		data[x].update({"Name of the router company": MACfromtext[x]})



	#Adding the service provider for the Network
	for i in range(len(SSID)):
		if SSID[i] == "":
			SSID2 = "Not found"
		else:
			SSID2 = SSID[i].upper()
		for x in range(len(Companies)):
			if SSID2.find(Companies[x]) > -1:
				FinalCompany.append(Company[x])
		if len(FinalCompany) == i:
			FinalCompany.append("Not Found")

	for x in range(len(data)):
		data[x].update({"Name of the service provider": FinalCompany[x]})


	#Adding the router model
	for i in range(len(MACshort)):
		SUMA= FinalCompany[i]+MACshort[i].upper()
		for line in file4:
			line = line.strip()
			if re.match(SUMA,line):
				Routers.append(line[31:])
		if len(Routers) ==i:
			Routers.append("Not Found")
		file4.seek(0)

	for x in range(len(data)):
		data[x].update({"Model of the router": Routers[x]})



# Creating the new json document
	with open("dataOutput.json", 'w') as f:
		json.dump(data, f, indent=4)
