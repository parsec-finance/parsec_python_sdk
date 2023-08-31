from parsecfi import Parsec
from datetime import datetime, timedelta
import pandas as pd
import matplotlib.pyplot as plt

API_KEY = ""
parsec = Parsec(API_KEY)

# Get the current date and time
current_datetime = datetime.now()
week_ago = current_datetime - timedelta(days=7)
since = int(week_ago.timestamp())

CHAIN = "base"
FRIEND_TECH = "0xcf205808ed36593aa40a44f10c7f7c2f67d4a4d4"
HANDLE = '@HsakaTrades'

ADDRESS = parsec.address(variables={'name': HANDLE})['address']

vars = {
	'address': FRIEND_TECH,
	'chain': CHAIN,
	'log': "Trade",
	'since': since,
    'filters': [{
        'comparator': '=',
        'input': 'subject',
        'value': ADDRESS
    }]
}

df = parsec.contract_logs(variables=vars)
df['datetime'] = pd.to_datetime(df['timestamp'], unit='s')
df['eth_price'] = df['ethAmount'] / df['shareAmount']     

plt.figure(figsize=(10, 6))
plt.plot(df['datetime'], df['eth_price'], marker='o')
plt.xlabel('Timestamp')
plt.ylabel('Price')
plt.title(f'{HANDLE} Price Over time')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()
plt.show()