import pandas as pd

query_string = """
  query TrendingContracts($chain: String!, $sortBy: String!, $limit: Int!, $lookback: String!) {
    trendingContracts(
      chain: $chain
      sortBy: $sortBy
      limit: $limit
      lookback: $lookback
    ) {
      address
      chain
      usage {
        ethSent
        gas
        gasPrev
        nTxs
        senders
        sendersChange
        sendersPrev
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
  data = json_data['trendingContracts']

  for item in data:
    for key, val in item['usage'].items():
      item[key] = val
    del item['usage']

  return pd.DataFrame(data)