
## Parsec API
python SDK to interact with the [parsec](https://parsec.finance) API

#### Getting Started
Retrive your api key from the parsec app, located in:
`Settings -> Subscription -> api key`
It will be of the form `par_ak_ + ...`

#### Usage
```
pip install parsecfi
```

```
API_KEY = "<YOUR API KEY>"
parsec = Parsec(API_KEY)

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
```

See `/examples` for more examples and `/parsecfi/lib/endpoints` for queries and necessary variables. If a query is missing please file an issue!

/parsec
