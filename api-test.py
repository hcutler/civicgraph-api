import json
import urllib
import requests
import urllib2

# Categories
# Returns json object with all categories and their associated id.
# URL: /api/categories
# Method: GET
# URL Params
## Required: 
## Data Params: url, data
## Success Response: 200
## Error Response: 
# (1) 404 Client Error: NOT FOUND
###: requests.exceptions.HTTPError: 404 Client Error: NOT FOUND for url: http://civicgraph.io/api/categoriez
# (2) 405 METHOD NOT ALLOWED
## Sample Call:
url = "http://civicgraph.io/api/categories"
data = '{"query":{"categories":[{"id"}]}'

response = requests.put(url, data=data)
if (response.ok):
  jData = json.loads(response.content)
  for key in jData:
    print jData[key]
else:
  print response.raise_for_status()


# connections
# URL: /api/connections
# Method: GET
# URL Params
## Required: 
## Data Params:
## Success Response: 200
## Error Response: 405 METHOD NOT ALLOWED
## Sample Call:

# url = "http://civicgraph.io/api/connections"
# data = '{"query":{"connections":{}}'
# response = requests.get(url, data=data)

# if (response.ok):
#   jData = json.loads(response.content)
#   for key in jData:
#     print jData[key]
# else:
#   print response.raise_for_status()

# entities
# URL: /api/entities
# Method: GET
# URL Params
## Required: 
## Data Params:
## Success Response:
## Error Response:

# requests.exceptions.ConnectionError: HTTPConnectionPool(host='civicgraph.io', port=80): Max retries exceeded with url: /api/categories (Caused by NewConnectionError('<requests.packages.urllib3.connection.HTTPConnection object at 0x10333bb10>: Failed to establish a new connection: [Errno 8] nodename nor servname provided, or not known',))


# ## Sample Call:
# url = "http://civicgraph.io/api/connections"
# data = '{"query":{"nodes":{}}'
# response = requests.get(url, data=data)

# if (response.ok):
#   jData = json.loads(response.content)
#   for key in jData:
#     print jData[key]
# else:
#   print response.raise_for_status()





# data = '{"query":{"bool":{"must":[{"text":{"record.document":"SOME_JOURNAL"}},{"text":{"record.articleTitle":"farmers"}}],"must_not":[],"should":[]}},"from":0,"size":50,"sort":[],"facets":{}}'
# response = requests.get(url, data=data)



#OLD STUFF
# url = "https://civicinsight.azurewebsites.net/athena"
# response = urllib.urlopen(url)
# contents = response.read() #returns type 'string'

# text = contents.decode('utf8') #returns type 'unicode'

# all_data = json.loads(text) #returns type 'json'

# nodes = json.dumps(all_data['nodes'], indent=4)
# print nodes