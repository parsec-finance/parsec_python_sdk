import pandas as pd

query_string = """
  query TokenDeltas($address: String, $limit: Integer!, $lookback: String!, $chain: String!) {
    token(address: $address, chain: $chain) {
      balanceChanges(limit: $limit, lookback: $lookback) {
        delta
        balanceStart
        balanceEnd
        bought
        sold
        chain
        address
        addressLabel {
          label
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
  return pd.DataFrame(json_data['token']['balanceChanges'])

def help():
  f"Find the largest token deltas over an interval"