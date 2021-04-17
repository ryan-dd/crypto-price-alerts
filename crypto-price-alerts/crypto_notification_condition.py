from enum import Enum
from pycoingecko import CoinGeckoAPI 
import time
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
        self.notify_triggered = False
        
    def should_notify(self):
        self.current_price = self._get_price()

        # Don't notify more than once
        if self.notify_triggered:
            return False
        else:
            if self.above_or_below == Threshold.ABOVE:
                self.notify_triggered = self.current_price > self.threshold_usd
            elif self.above_or_below == Threshold.BELOW:
                self.notify_triggered = self.current_price < self.threshold_usd
            return self.notify_triggered
    
    def _get_price(self):
        cg = CoinGeckoAPI()
        response = cg.get_price(ids=self.name_of_coin, vs_currencies='usd')
        return response[self.name_of_coin]['usd']
        
    def get_email_message(self):
        return """\
Subject: PRICE UPDATE """ + self.name_of_coin + """

"""+ self.name_of_coin + " is now at " + str(self.current_price) + " USD, " + self.above_or_below.value + " " + str(self.threshold_usd) + " USD"
        