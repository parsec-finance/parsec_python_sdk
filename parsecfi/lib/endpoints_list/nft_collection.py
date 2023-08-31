

import pandas as pd

query_string = """
  query NftCollection($address: String!) {
    nftCollection(address: $address) {
      name
      floor
      address
      chain
      holdersCount
      floor1dDelta
      floor7dDelta
      floor30dDelta
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