import requests
import time

RawData = requests.get("https://api.frankfurter.app/latest?amount=1&from=USD&to=EUR")
Data = RawData.json()
user_input = int(input("Enter the amount of USD: "))
time.sleep(1)
print("On today's market: ")
for key , value in Data.items():
    print("{} : {}".format(key,value))
    time.sleep(0.5)

print("Converted USD: ",Data['rates']['EUR'] *user_input," EUR")
time.sleep(5)