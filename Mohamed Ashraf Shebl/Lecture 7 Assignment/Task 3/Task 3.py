import requests
import time
import csv
import os
os.chdir('Task 3')
RawData = requests.get("https://gorest.co.in/public-api/users?_format=json&access-token=H4lYmIGLXZkDlpy_w0ZVS5rgcpDXbN7fhRRy")
Data = RawData.json()

with open('gorest.csv','a',newline='') as f:
    writer=csv.writer(f)
    writer.writerow(['Name','Email','Gender','Status'])
    for data in Data['data']:
        Name = data['name']
        Email = data['email']
        Gender = data['gender']
        Status = data['status']
        if Status == "inactive":
            Status = 0
        else:
            Status = 1
        writer.writerow([Name,Email,Gender,Status])
