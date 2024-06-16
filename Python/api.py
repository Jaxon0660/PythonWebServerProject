import requests 
import json

response = requests.get("https://replit.com/@TomiTokko/api#manage.py")

print(response.status_code)

res = json.loads(response.text)

#print(res)

for data in res:
    print(data)