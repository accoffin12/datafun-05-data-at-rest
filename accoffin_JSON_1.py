"""
Loading JSON text using accounts example.
"""
import json
accounts_dict = {'accounts': [
    {'account': 120, 'name': 'Jones', 'balance': 24.98},
    {'account': 122, 'name': 'Barns', 'balance': 385.67},
    {'account': 124, 'name': 'Whyte', 'balance': 0.00},
    {'account': 126, 'name': 'Stone', 'balance': -41.25},
    {'account': 128, 'name': 'Carter', 'balance': 227.39}

]}

with open('accounts.json', 'r') as accounts:
    accounts_json = json.load(accounts)