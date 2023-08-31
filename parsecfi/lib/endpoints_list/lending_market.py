import pandas as pd

query_string = """
	query LendingMarket($symbol: String!, $protocol: String!) {
		lendingMarket(symbol: $symbol, protocol: $protocol) {
			poolId
			poolName
			protocol
			supplyRate
			borrowRate
			collatRatio
			history(interval: "1d", limit: 30) {
				borrowRate
				supplyRate
				totalSupplied
				totalBorrows
				borrowRewards {
				rateBase
				rewardToken
			}
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
	return pd.DataFrame(json_data['lending_market'])