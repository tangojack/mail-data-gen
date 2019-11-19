import pandas as pd
import json
import uuid
from randomtimestamp import randomtimestamp
import random
from random import seed

x_train = []
y_train = []
for i in range(0, 100):
    actions = {}
    mail_item = {}
    mail_item['id'] = uuid.uuid1();
    mail_item['is_read'] = bool(random.getrandbits(1))
    mail_item['replied_to'] = bool(random.getrandbits(1))
    mail_item['importance'] = random.choice(['Important', 'Normal'])
    mail_item['time_received'] = randomtimestamp(start_year=2019, text=True)
    mail_item['to'] = bool(random.getrandbits(1))
    mail_item['cc'] = bool(random.getrandbits(1))
    mail_item['bcc'] = bool(random.getrandbits(1))
    mail_item['sender'] = random.choice(['rfq-dev', 'rfq-qa', 'dbau', 'tap-team', 'mumbai-athena'])
    mail_item['receiver'] = random.choice(['miranvin', 'mumbai-athena', 'hkgrad'])
    mail_item['folder'] = random.choice(['inbox', 'test', 'rfq', 'important'])
    actions['user_action'] = random.choice(['nothing', 'bin', 'spam', 'important'])
    x_train.append(mail_item)
    y_train.append(actions)


x_train_df = pd.DataFrame(x_train)
y_train_df = pd.DataFrame(y_train)


x_train_df.to_pickle("x_train.pkl")
y_train_df.to_pickle("y_train.pkl")
