import pandas as pd

query_string = """
  query TokenHolders($address: String!, $chain: String!, $limit: Int!) {
    token(address: $address, chain: $chain) {
      topHolders(limit: $limit) {
        balance
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
  return pd.DataFrame(json_data['token']['topHolders'])
