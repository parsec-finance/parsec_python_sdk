import pandas as pd

query_string = """
  query Trades(
    $since: Int,
    $before: Int,
    $from: String,
    $taker: String,
    $maker: String,
    $pair: String,
    $side: String,
    $sort: [String],
    $tx: String,
    $venue: String,
    $limit: Int!
  ) {
    trades(limit: $limit) {
      venue
      baseAmount
      from
      pair
      price
      quoteAmount
      side
      timestamp
    }
  }
"""

def query(variables):
  return {
    'query': query_string,
    'variables': variables
  }

def parser(json_data):
  return pd.DataFrame(json_data['trades'])