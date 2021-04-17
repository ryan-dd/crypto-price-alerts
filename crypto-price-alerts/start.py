from crypto_notification_condition import CryptoNotificationCondition, Threshold
from email_sender import EmailSender

import time
import argparse

parser = argparse.ArgumentParser(description='Send notifications on crypto prices')
parser.add_argument('gmail_sender_address', type=str, help='Gmail address to send from')
parser.add_argument('email_receiver_address', type=str, help='Email Address to send to')
args = parser.parse_args()

email_sender = EmailSender(args.gmail_sender_address)
condition1 = CryptoNotificationCondition('bitcoin', Threshold.ABOVE, 70000)
condition2 = CryptoNotificationCondition('bitcoin', Threshold.BELOW, 60000)
conditions = [condition1, condition2]

print("Starting...")
# Use Ctrl+C to exit
while(True):
    for condition in conditions:
        if condition.should_notify():
            email_sender.send_email(condition.get_email_message(), args.email_receiver_address)
    # CoinGecko reportedly updates every 1 - 10 minutes
    time.sleep(60)


