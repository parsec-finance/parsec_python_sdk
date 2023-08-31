import json
import pandas as pd

query_string = """
	query Transfers(
		$address: String, 
		$to: String,
		$chain: String,
		$from: String,
		$toOrFrom: String,
		$toOrFroms: [String],
		$tx: String,
		$block: Int,
		$limit: Int,
		$offset: Int
	) {
		transfers(
			address: $address,
			chain: $chain, 
			to: $to,
			from: $from, 
			toOrFrom: $toOrFrom,
			toOrFroms: $toOrFroms,
			tx: $tx,
			block: $block,
			limit: $limit,
			offset: $offset
		) {
			to
		    from
		    value
		    timestamp
		    tx
		    address
		    decimals
		    usd_price
		    usd_value
		    symbol
		    img_src
		    chain
		    is_nft
		}
	}
"""

def query(variables):
	return {
		'query': query_string,
		'variables': variables
	}

def parser(json_data):
	return pd.DataFrame(json_data['transfers'])