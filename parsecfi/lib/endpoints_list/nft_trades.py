import pandas as pd

query_string = """
  query NftTrades(
    $limit: Int!, 
    trader: $trader, 
    traits: [[String]], 
    since: Int,
    before: Int,
    collectionAddress: String,
    tokenId: String
    exchange: String
  ) {
    nftTrades(limit: $limit) {
      chain
      price
      side
      usdValue
      thumbnailUrl
      tokenId
      taker
      maker
      timestamp
      usdValue
      collectionAddress
      collectionName
      exchange
      tx
    }
  }
"""

def query(variables):
  return {
    'query': query_string,
    'variables': variables
  }

def parser(json_data):
  return pd.DataFrame(json_data['nftTrades'])