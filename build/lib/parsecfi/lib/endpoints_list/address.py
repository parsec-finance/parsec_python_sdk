import pandas as pd

query_string = """
  query Address($name: String, $address: String) {
    address(name: $name, address: $address) {
      name
      address
    }
  }
"""

def query(variables):
  return {
    'query': query_string,
    'variables': variables
  }

def parser(json_data):
  return json_data['address']