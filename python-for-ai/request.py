import requests


#download a webpage
response = requests.get("https://api.github.com")
print(response.status_code)