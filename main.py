import requests
import keys

def detect():
    ip = input(': ')
    url = f'https://vpnapi.io/api/{ip}?key={keys.api_key}'
    res = requests.get(url)
    print(res.json())

detect()