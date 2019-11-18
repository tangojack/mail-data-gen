import pandas as pd
import json
import uuid
from randomtimestamp import randomtimestamp
import random
from random import seed

mail_items = []
for i in range(0, 100):
    mail_item = {}
    mail_item['id'] = uuid.uuid1();
    mail_item['isRead'] = bool(random.getrandbits(1))
    mail_item['repliedTo'] = bool(random.getrandbits(1))
    mail_item['importance'] = random.choice(['Important', 'Normal'])
    mail_item['timeOpened'] = randomtimestamp(start_year=2019, text=True)
    mail_item['to'] = bool(random.getrandbits(1))
    mail_item['cc'] = bool(random.getrandbits(1))
    mail_item['bcc'] = bool(random.getrandbits(1))
    mail_item['sender'] = random.choice(['rfq-dev', 'rfq-qa', 'dbau', 'tap-team', 'mumbai-athena'])
    mail_item['receiver'] = random.choice(['miranvin', 'mumbai-athena', 'hkgrad'])
    mail_items.append(mail_item)

df = pd.DataFrame(mail_items)
df.to_pickle("mail_items.pkl")
