import requests
import time
import csv

RawData = requests.get("https://www.metaweather.com/api/location/1521894/")
Data = RawData.json()

with open("metaweather.csv","a",newline="") as f:
    writer = csv.DictWriter(f,fieldnames=['Temperature','Humidity','Visibility','Air Pressure','Wind Speed','Datetime'])
    writer.writeheader()
    for ID in Data['consolidated_weather']:
        ID_Temp =  ID['the_temp']
        ID_Humid = ID['humidity']
        ID_Visibility = ID['visibility']
        ID_Air_Pressure = ID['air_pressure']
        ID_Wind_Speed = ID['wind_speed']
        ID_Datetime = ID['created']
        writer.writerow({'Temperature':ID_Temp, 'Humidity':ID_Humid, 'Visibility': ID_Visibility, 'Air Pressure':ID_Air_Pressure, 'Wind Speed':ID_Wind_Speed, 'Datetime':ID_Datetime})