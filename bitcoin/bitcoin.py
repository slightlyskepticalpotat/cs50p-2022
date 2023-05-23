import requests, sys, json

if len(sys.argv) == 1:
    sys.exit("Missing command-line argument")
try:
    btc = float(sys.argv[1])
except:
    sys.exit("Command-line argument is not a number")
price = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
price = float(price.json()["bpi"]["USD"]["rate"].replace(",", "")) * btc
print(f"${price:,.4f}")
