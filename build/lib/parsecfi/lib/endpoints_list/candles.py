import pandas as pd

query_string = """
  query GetCandles($interval: String!, $limit: Int!, $pair: String!, $venue: String!) {
    candles(interval: $interval, limit: $limit, pair: $pair, venue: $venue) {
      data
      derived
      exchange
      interval
      pair
    }
  }
"""

def query(variables):
  return {
    'query': query_string,
    'variables': variables
  }

def parser(json_data):
  return pd.DataFrame(json_data['candles'])