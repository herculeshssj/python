import requests
import json
from pymongo import MongoClient

# Define the API endpoint URL
url = 'https://api.semanticscholar.org/graph/v1/paper/search/bulk'

# More specific query parameter
# Queries
# - ("web of things") | WoT
# - web of things
query_params = {
   'query': '("web of things") | WoT',
   'fields': 'paperId,title,year,abstract,externalIds,url,authors,referenceCount,citationCount,publicationTypes,journal'
}

# Directly define the API key (Reminder: Securely handle API keys in production environments)
api_key = 'api_key'  # Replace with the actual API key

# Define headers with API key
headers = {'x-api-key': api_key}

# Conexão com a base Mongo
client = MongoClient('mongodb://s2api:S2s3m4nt1cSch*l4r@localhost:27017')
db = client.s2api

while True:
   # Send the API request
   response = requests.get(url, params=query_params, headers=headers)

   # Check response status
   if response.status_code == 200:
      response_data = response.json()
      # Process and print the response data as needed
      #pretty_json = json.dumps(response_data, indent=4)
      #print(pretty_json)
      #print(response_data)

   for s2result in response_data['data']:
      s2pretty = json.dumps(s2result, indent=4)
      print(s2pretty)
      print('**************************************************')

      db.bulk_search.insert_one(s2result)

   else:
      print(f"Request failed with status code {response.status_code}: {response.text}")

   if response_data['token'] is None or response_data['token'] == '':
      break
   else:
      query_params['token'] = response_data['token'];

# Encerra a conexão com a base Mongo
client.close()

