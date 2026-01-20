import requests
import sys

if len(sys.argv) == 1:
    sys.exit("Missing command-line argument")

try:
    num = float(sys.argv[1])
except:
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=6bbd4db16aa06a93fdcb331e8b522cae1df20b85f4e63152613ef05f65d3458c")
    data1 = response.json()
    bitcoin = float(data1['data']['priceUsd'])
    amount = num * bitcoin
    print(f"${amount:,.4f}")
except requests.RequestException:
    sys.exit()
