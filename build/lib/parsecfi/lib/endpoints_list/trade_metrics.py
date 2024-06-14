import pandas as pd

query_string = """
  query TradeMetricsBins($chains: [String], $limit: Int!, $interval: String, $offset: Int, $venues: [String], $pairs: [String]) {
	tradeMetricsBins(chains: $chains, limit: $limit, interval: $interval, offset: $offset, venues: $venues, pairs: $pairs) {
	  uniqueTakers
	  volumeUsd
	  nTrades
	  startTs
	  endTs
	}
  }
"""

def query(variables):
  return {
    'query': query_string,
    'variables': variables
  }

def parser(json_data):
  return pd.DataFrame(json_data['tradeMetricsBins'])