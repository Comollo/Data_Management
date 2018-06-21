### Trasform CSV in Dict

## GERMANY

import csv

Germany = open("germany.csv", "r", encoding="utf-8") #open file
fieldnames = ("Category","OSM - id","Latitude","Longitude","Place")
reader = csv.DictReader(Germany, fieldnames, delimiter = "|")
germany_list =[]
for line in reader:
    germany_list.append(line)

for i in range(len(germany_list)):
    germany_list[i] = dict(germany_list[i].items()) 

for i in range(len(germany_list)):
    germany_list[i]["Category"] = int(germany_list[i]["Category"])
    germany_list[i]["Latitude"] = float(germany_list[i]["Latitude"])
    germany_list[i]["Longitude"] = float(germany_list[i]["Longitude"]) #transform value in interger, float...

### Check empty dict
for i in range(len(germany_list)):
    if bool(germany_list[i]["Category"] and germany_list[i]["Latitude"]
           and germany_list[i]["Longitude"] and germany_list[i]["OSM - id"] and germany_list[i]["Place"]) == False:
        print(i)

#close file
Germany.close() #close file 


## ITALY

italy = open("italy.csv", "r", encoding="utf-8") #open file
fieldnames = ("Category","OSM - id","Latitude","Longitude","Place")
reader = csv.DictReader(italy, fieldnames, delimiter = "|")
italy_list =[]
for line in reader:
    italy_list.append(line)

for i in range(len(italy_list)):
    italy_list[i] = dict(italy_list[i].items()) 

for i in range(len(italy_list)):
    italy_list[i]["Category"] = int(italy_list[i]["Category"])
    italy_list[i]["Latitude"] = float(italy_list[i]["Latitude"])
    italy_list[i]["Longitude"] = float(italy_list[i]["Longitude"]) #transform value in interger, float...

### Check empty dict

for i in range(len(italy_list)):
    if bool(italy_list[i]["Category"] and italy_list[i]["Latitude"]
           and italy_list[i]["Longitude"] and italy_list[i]["OSM - id"] and italy_list[i]["Place"]) == False:
        print(i)

#close file
italy.close()


## SPAIN

Spain = open("spain.csv", "r", encoding="utf-8") #open file
fieldnames = ("Category","OSM - id","Latitude","Longitude","Place")
reader = csv.DictReader(Spain, fieldnames, delimiter = "|")
spain_list =[]
for line in reader:
    spain_list.append(line)

for i in range(len(spain_list)):
    spain_list[i] = dict(spain_list[i].items()) 

### Check empty dict
#for i in range(len(spain_list)):
#   if bool(spain_list[i]["Category"] and spain_list[i]["Latitude"]
#           and spain_list[i]["Longitude"] and spain_list[i]["OSM - id"] and spain_list[i]["Place"]) == False:
#        print(i)

spain_list.remove(spain_list[79728])
spain_list.remove(spain_list[79728])

for i in range(len(spain_list)):
    spain_list[i]["Category"] = int(spain_list[i]["Category"])
    spain_list[i]["Latitude"] = float(spain_list[i]["Latitude"])
    spain_list[i]["Longitude"] = float(spain_list[i]["Longitude"]) #transform value in interger, float...

#close file
Spain.close()

## FRANCE

France = open("france.csv", "r", encoding="utf-8") #open file
fieldnames = ("Category","OSM - id","Latitude","Longitude","Place")
reader = csv.DictReader(France, fieldnames, delimiter = "|")
france_list =[]
for line in reader:
    france_list.append(line)

for i in range(len(france_list)):
    france_list[i] = dict(france_list[i].items()) 

### Check empty dict
#for i in range(len(france_list)):
#    if bool(france_list[i]["Category"] and france_list[i]["Latitude"]
#           and france_list[i]["Longitude"] and france_list[i]["OSM - id"] and france_list[i]["Place"]) == False:
#        print(i)

france_list.remove(france_list[41349])

for i in range(len(france_list)):
    france_list[i]["Category"] = int(france_list[i]["Category"])
    france_list[i]["Latitude"] = float(france_list[i]["Latitude"])
    france_list[i]["Longitude"] = float(france_list[i]["Longitude"]) #transform value in interger, float...

#close file
France.close()


## GREAT-BRITAIN

GB = open("great-britain.csv", "r", encoding="utf-8") #open file
fieldnames = ("Category","OSM - id","Latitude","Longitude","Place")
reader = csv.DictReader(GB, fieldnames, delimiter = "|")
gb_list =[]
for line in reader:
    gb_list.append(line)

for i in range(len(gb_list)):
    gb_list[i] = dict(gb_list[i].items()) 

for i in range(len(gb_list)):
    gb_list[i]["Category"] = int(gb_list[i]["Category"])
    gb_list[i]["Latitude"] = float(gb_list[i]["Latitude"])
    gb_list[i]["Longitude"] = float(gb_list[i]["Longitude"]) #transform value in interger, float...

for i in range(len(gb_list)):
    if bool(gb_list[i]["Category"] and gb_list[i]["Latitude"]
           and gb_list[i]["Longitude"] and gb_list[i]["OSM - id"] and gb_list[i]["Place"]) == False:
        print(i)

#close file
GB.close()