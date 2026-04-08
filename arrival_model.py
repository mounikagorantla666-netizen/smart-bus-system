import requests

url = "https://www.apsrtconline.in/oprs-web/services/cancel.do"
response = requests.get(url)
data = response.json()

print(data)