import json
import urllib
import requests
import urllib2

# Get Categories
# Returns json object with all categories and their corresponding integer ID.
# URL: /api/categories
# Method: GET
## Success Response: 200
## Error Response: 404, 405, or 413

# Sample Call:
url = "http://civicgraph.io/api/categories"
data = '{"query":{"categories":[{}]}'

response = requests.get(url, data=data)
if (response.ok):
  jData = json.loads(response.content)
  for key in jData:
    print jData[key]
else:
  print response.raise_for_status()


# Get Connections
# Returns json object with all connections (grouped by connection type) with source and target ids for each connection.
# URL: /api/connections
# Method: GET
# # Success Response: 200
# # Error Response: 404, 405, or 413

## Sample Call:
url = "http://civicgraph.io/api/connections"
data = '{"query":{"connections":{}}'
response = requests.get(url, data=data)
print response.content

if (response.ok):
  jData = json.loads(response.content)
  for key in jData:
    print JData[key] #print all connection types
    print jData[key]["Employment"] #print only Employment connections
    print jData[key]["Collaboration"] #print only Collaboration connections
    print jData[key]["Data"] #print only Data connections
    print jData[key]["Funding"] #print only Funding connections
    print jData[key]["Relation"] #print only Relation connections
else:
  print response.raise_for_status()

# Get Entities
# Returns JSON object of all entity data.
# URL: /api/entities
# Method: GET
## Success Response: 200
## Error Response: 404, 405, or 413

## Sample Call:
url = "http://civicgraph.io/api/entities"
print url
data = '{"query":{"nodes":{}}'
response = requests.get(url, data=data)

if (response.ok):
  jData = json.loads(response.content)
  for key in jData:
    print jData[key]
else:
  print response.raise_for_status()
