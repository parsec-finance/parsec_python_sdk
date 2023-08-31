from parsecfi.lib.endpoints_list import (
	lending_market, 
	contract_logs, 
	token_holders, 
	token_acc, 
	trending_contracts,
	transfers,
	address
)

def load():
	return {
		'lending_market': lending_market,
		'contract_logs': contract_logs,
		'token_holders': token_holders,
		'token_acc': token_acc,
		'trending_contracts': trending_contracts,
		'transfers': transfers,
		'address': address
	}