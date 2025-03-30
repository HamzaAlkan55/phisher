import requests

ip = requests.get("https://api64.ipify.org?format=json").json()["ip"]
print(f"Senin IP adresin: {ip}")
import requests

ip = requests.get("https://api64.ipify.org?format=json").json()["ip"]
print(f"Senin IP adresin: {ip}")
