import requests
import sys


def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    try:
        num_bitcoin = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
    try:
        res = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        res.raise_for_status()
    except requests.RequestException:
        sys.exit("Error fetching from CoinDesk API")
    data = res.json()
    try:
        btc_price_usd = data["bpi"]["USD"]["rate_float"]
    except (KeyError,TypeError,ValueError):
        sys.exit("Error while parsing")
    cost = num_bitcoin * btc_price_usd

    print(f"${cost:,.4f}")
    

if __name__ == "__main__":
    main()