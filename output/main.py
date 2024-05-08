import requests

url = "https://example.com/api/submit"
headers = {'Content-Type': 'application/json'}

with open('main.py', 'r') as f:
    data = eval(f.read())

response = requests.post(url, headers=headers, json=data)
print(response.json())