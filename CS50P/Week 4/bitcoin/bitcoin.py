import sys
import requests

try:
    if len(sys.argv) < 2:
        sys.exit('Missing command-line argument')
    bitcoin = float(sys.argv[1])
except ValueError:
    sys.exit('Command-line argument is not a number')

try:
    req = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json').json()
except (requests.RequestException, requests.Timeout, requests.ConnectionError):
    sys.exit('Something went wrong trying to get bitcoin price!')

bitcoin_price = float((req['bpi']['USD']['rate']).replace(',', ''))

usd_price = bitcoin_price * bitcoin

print(f'${usd_price:,.4f}')