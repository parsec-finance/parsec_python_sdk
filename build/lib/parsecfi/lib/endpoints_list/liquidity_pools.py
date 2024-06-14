import pandas as pd

query_string = """
  query LiquidityPools($limit: Int!, $orderBy: String!, $orderDir: String!, $protocol: String, $symbol: String) {
    liquidityPools(
      limit: $limit
      orderBy: $orderBy
      orderDir: $orderDir
      protocol: $protocol
      symbol: $symbol
    ) {
      address
      swapFee
      protocol
      reserveUsd
      volumeUsd
      vlmLiqRatio
      tokens {
        symbol
        balance
        weight
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
  return pd.DataFrame(json_data['liquidityPools'])