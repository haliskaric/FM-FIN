import requests

def get_description(api_key, symbol):
    url = f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={symbol}&apikey={api_key}'
    r = requests.get(url)
    data = r.json()
    return data.get('Description', f'Description not found for {symbol}')

# Replace the 'your_api_key' below with your own key from https://www.alphavantage.co/support/#api-key
api_key = 'YYIYJPK1IZ9SISF1'
ticker_symbols = ['IBM', 'AAPL', 'GOOGL', 'MSFT']

for symbol in ticker_symbols:
    description = get_description(api_key, symbol)
    print(f'{symbol}: {description}\n')
