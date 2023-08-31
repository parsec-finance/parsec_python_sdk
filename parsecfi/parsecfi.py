import sys
sys.path.append('./lib')

import requests
import json
import pandas as pd
from parsecfi.lib import endpoints

BASE_URL = "https://api.parsec.finance/api/v2"

class Parsec:
	def __init__(self, ak):
		self.api_key = ak
		self.endpoints = endpoints.load()

	def api_call(self, endpoint, variables):
		json_data = endpoint.query(variables)
		r = requests.post(BASE_URL, json=json_data, headers={'api_key': self.api_key})
		if r.status_code == 200:
			text = json.loads(r.text)
			if 'data' in text:
				return endpoint.parser(text['data'])
			else:
				return text
		else:
			return f"Error: {r.status_code}"

	def __getattr__(self, name):
		if name in self.endpoints:
			return lambda variables: self.api_call(endpoint=self.endpoints[name], variables=variables)
		else:
			raise AttributeError(f"'Parsec' object has no attribute '{name}'")
