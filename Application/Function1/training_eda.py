
import requests

url = "http://localhost:8890/tree/Videos/test.json"
response = requests.get(url)

data = response.json()
for video in data['feed']['entry'][0:6]:
  print(video['title']['$t'])