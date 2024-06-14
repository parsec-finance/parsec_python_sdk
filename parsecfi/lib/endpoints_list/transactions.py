import json
import pandas as pd

query_string = """
  query ApiTxs($addresses: [String!]!, $limit: Int!, $chains: [String], $offset: Int, $call: String, $to: String, $from: String, $since: Int, $before: Int) {
    txs(
      addresses: $addresses
      limit: $limit
      chains: $chains
      offset: $offset
      functionCall: $call
      to: $to
      from: $from
      since: $since
      before: $before
    ) {
      chain
      block
      hash
      to
      from
      gasPrice
      gasUsed
      input
      call
      status
      index
      value
      timestamp
      meta
      contract_creation
      marketData {
        type
        data
        __typename
      }
      inputDecoded {
        function
        args
        __typename
      }
      message
      __typename
    }
  }
"""

def query(variables):
  return {
    'query': query_string,
    'variables': variables
  }

def parser(json_data):
  return pd.DataFrame(json_data['txs'])