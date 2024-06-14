import pandas as pd

query_string = """
  query LpPositions($poolAddress: String!, $inRangeOnly: Boolean!, $exchange: String!, $limit: Int!) {
    liquidityPool(poolAddress: $poolAddress, exchange: $exchange) {
      positions(limit: $limit, inRangeOnly: $inRangeOnly) {
        deltaQuote
        feeBps
        nav
        pair
        positionId
        price
        provider
        tickLowerPrice
        tickUpperPrice
        addressLabel {
          src
          label
          address
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
  return pd.DataFrame(json_data['liquidityPool']['positions'])