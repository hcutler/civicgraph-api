import json
import urllib

url = "https://civicinsight.azurewebsites.net/athena"
response = urllib.urlopen(url)
contents = response.read()

text = contents.decode('utf8')
all_data = json.loads(text)

#Sample functions to access data in Civic Graph database

#Operation: Get all data
#Input: 'dict'
#Output: 'dict'
def get_data(all_data):
  return all_data


#Operation: Get all collaboration connections
#Input: 'dict'
#Output: 'dict'
def get_collaboration_connection(collaboration_connections):
  return collaboration_connections


#Operation: Get all nodes
#Input: 'dict'
#Output: 'dict'
def get_nodes(nodes):
  return nodes


#Operation: Get all data connections
#Input: 'dict'
#Output: 'dict'
def get_data_connections(data_connections):
  return data_connections


#Operation: Get all funding connections
#Input: 'dict'
#Output: 'dict'
def get_funding_connections(funding_connections):
  return funding_connections

#Operation: Get all investment connections
#Input: 'dict'
#Output: 'dict'
def get_investment_connections(investment_connections):
  return investment_connections


def main():
  # get_collaboration_connection(all_data)
  # get_nodes(all_data)
  # get_data_connections(all_data)
  # get_funding_connections(all_data)
  # get_investment_connection(all_data)


if __name__ == "__main__":
    main()
