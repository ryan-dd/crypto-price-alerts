from enum import Enum
from pycoingecko import CoinGeckoAPI 

class Threshold(Enum):
    ABOVE = "above"
    BELOW = "below"

class CryptoNotificationCondition:
    def __init__(self, name_of_coin, above_or_below, threshold_usd):
        # Name of coin should match CoinGeckoAPI coin ID
        self.name_of_coin = name_of_coin
        self.above_or_below = above_or_below
        self.threshold_usd = threshold_usd
        self.current_price = 0
        
    def should_notify(self):
        self.current_price = self._get_price()
        
        if self.above_or_below == Threshold.ABOVE:
            return self.current_price > self.threshold_usd
        if self.above_or_below == Threshold.BELOW:
            return self.current_price < self.threshold_usd
    
    def _get_price(self):
        cg = CoinGeckoAPI()
        response = cg.get_price(ids=self.name_of_coin, vs_currencies='usd')
        return response[self.name_of_coin]['usd']
        
    def get_email_message(self):
        return """\
Subject: PRICE UPDATE """ + self.name_of_coin + """

"""+ self.name_of_coin + " is now at " + str(self.current_price) + " USD, " + self.above_or_below.value + " " + str(self.threshold_usd) + " USD"
        