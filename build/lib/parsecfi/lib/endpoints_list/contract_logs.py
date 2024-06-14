import json
import pandas as pd

query_string = """
	query ContractLogs(
		$address: String!, 
		$chain: String!, 
		$log: String!,
		$since: Int,
		$limit: Int,
		$filters: [LogFilter]
	) {
	  contract(address: $address, chain: $chain) {
	  	logs(limit: $limit, log: $log, since: $since, filters: $filters) {
	      timestamp
	      txId
	      data
	    }
	  }
	}
"""

def query(variables):
	return {
		'query': query_string,
		'variables': variables
	}

def parser(json_data):
	data = json_data['contract']['logs']

	for item in data:
		d = json.loads(item['data'])
		for key, val in d.items():
			item[key] = val
		del item['data']

	return pd.DataFrame(data)