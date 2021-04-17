from pycoingecko import CoinGeckoAPI 
import pprint

# Helper functions when trying to figure out which coin id goes to which token
def print_coin_list():
    cg = CoinGeckoAPI()
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(cg.get_coins_list())

def print_coin_price_usd(coin_id):
    cg = CoinGeckoAPI()
    response = cg.get_price(ids=coin_id, vs_currencies='usd')
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(response[coin_id]['usd'])

if __name__ == '__main__': 
    coin_id = 'ethereum'
    print_coin_price_usd(coin_id)