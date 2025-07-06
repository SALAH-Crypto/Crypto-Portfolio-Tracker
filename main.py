import requests

def get_price(symbol):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    return data[symbol]["usd"]

portfolio = {
    "bitcoin": 0.5,
    "ethereum": 2,
    "cardano": 1000
}

total_value = 0
for coin, amount in portfolio.items():
    price = get_price(coin)
    value = price * amount
    total_value += value
    print(f"{coin.title()}: ${price:.2f} x {amount} = ${value:.2f}")

print(f"Total Portfolio Value: ${total_value:.2f}")
