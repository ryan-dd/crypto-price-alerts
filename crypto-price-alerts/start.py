from crypto_notification_condition import CryptoNotificationCondition, Threshold
from email_sender import EmailSender

import time
import argparse
import sys

parser = argparse.ArgumentParser(description='Send notifications on crypto prices')
parser.add_argument('gmail_sender_address', type=str, help='Gmail address to send from')
parser.add_argument('email_receiver_address', type=str, help='Email Address to send to')
args = parser.parse_args()

email_sender = EmailSender(args.gmail_sender_address)

conditions = []
conditions.append(CryptoNotificationCondition('bitcoin', Threshold.ABOVE, 70000))
conditions.append(CryptoNotificationCondition('bitcoin', Threshold.BELOW, 10000))

print("Starting...")
while(True):
    try:
        for condition in conditions:
            if condition.should_notify():
                email_sender.send_email(condition.get_email_message(), args.email_receiver_address)
                print("Sent email: " + condition.name_of_coin)
    except:
        print("Error occurred")
        e1 = sys.exc_info()[0]
        e2 = sys.exc_info()[1]
        print(e1)
        print(e2)
    time.sleep(60)
