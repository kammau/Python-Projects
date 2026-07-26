import requests

url = "http://www.google.com"
response = requests.get(url)

print(f"Your request to: {url} \nCame back w/ status code {response.status_code}")