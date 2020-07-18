import requests

resp = requests.get("https://realpython.com")
html = resp.text

print(html[2:33])
