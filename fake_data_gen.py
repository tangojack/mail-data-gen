import pandas as pd
import json
import uuid
from randomtimestamp import randomtimestamp
import random

x_train = []
y_train = []
for i in range(0, 100):
    actions = {}
    mail_item = {}
    mail_item['id'] = uuid.uuid1();
    mail_item['is_read'] = random.getrandbits(1)
    mail_item['importance'] = random.choice(['Important', 'Normal'])
    mail_item['time_received'] = randomtimestamp(start_year=2019, text=True)
    mail_item['to'] = random.getrandbits(1)
    mail_item['cc'] = random.getrandbits(1)
    mail_item['bcc'] = random.getrandbits(1)
    mail_item['has_attachments'] = random.getrandbits(1)
    mail_item['sender'] = random.choice(['rfq-dev', 'rfq-qa', 'dbau', 'tap-team', 'mumbai-athena'])
    mail_item['receiver'] = random.choice(['miranvin', 'mumbai-athena', 'hkgrad'])
    mail_item['internal_or_external'] = random.choice(['internal', 'external'])

    actions['do_nothing'] = random.getrandbits(1) # will be retrieved using mails in inbox. afterwards whenever a user action is done.
    actions['move_to_bin'] = random.getrandbits(1) # will be retrieved using mails in bin for now. afterwards whenever a user action is done
    actions['move_to_important_folder'] = random.getrandbits(1) # will be retrieved using mails in important for now. afterwards whenever a user action is done
    # actions['reply_to_this_mail'] = bool(random.getrandbits(1))

    x_train.append(mail_item)
    y_train.append(actions)

x_train_df = pd.DataFrame(x_train)
y_train_df = pd.DataFrame(y_train)

x_train_df.to_pickle("x_train.pkl")
y_train_df.to_pickle("y_train.pkl")


# can be done with simple data mining
# actions['unsubscribe']
