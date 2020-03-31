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


# Adding data to the differents array separation
#Opening diferents txt neededs

file2 = open("ouis.txt", "r")
file3 = open("ouis2.txt", "r")


# Open the file like a dictionary
with open("data.json", "r+") as file:
    data = json.load(file)

    # Collecting all the data from the JSON
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

    # Adding the transmission channel value
    for x in range(len(data)):
        if Channel[x] <= 11:
            data[x].update({"Frecuency used": "2,5GHz"})
        else:
            data[x].update({"Frecuency used": "5GHz"})

    # Adding the fabricant name to the JSON
    #Making the MAC address short
    for mac in range(len(MAC)):
        MACshort.append(MAC[mac][:8])

    #Searching it in differents documents
    # for i in range(len(MACshort)):
    #     file2.seek(0)
    #     file3.seek(0)
    #     for line in file2:
    #         line = line.strip()
    #         if re.match(MACshort[i], line):
    #             MACfromtext.append(line[9:])
    #     if len(MACfromtext) == i:
    #         for line in file3:
    #             line = line.strip()
    #             string = MACshort[i][:2].upper(
    #             ) + '-' + MACshort[i][3:5].upper() + '-' + MACshort[i][6:8].upper()
    #             if re.match(string, line):
    #                 MACfromtext.append(line[18:])
    #         if len(MACfromtext) == i:
    #             MACfromtext.append("Not found")


    # for x in range(len(data)):
    #     data[x].update({"Name of the router company" : MACfromtext[x]})






# Creating the new json document
    # with open("data2.json", 'w') as f:
    #     json.dump(data, f, indent=4)

    
