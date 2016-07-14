import json
import urllib

url = "https://civicinsight.azurewebsites.net/athena"
response = urllib.urlopen(url)
contents = response.read() #returns type 'string'

text = contents.decode('utf8') #returns type 'unicode'

all_data = json.loads(text) #returns type 'json'

nodes = json.dumps(all_data['nodes'], indent=4)
print nodes


