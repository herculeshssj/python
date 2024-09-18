import requests
import json
from pymongo import MongoClient

# Define the API endpoint URL
url = 'https://api.semanticscholar.org/graph/v1/paper/search'

# More specific query parameter
query_params = {
   'query': 'web of things',
   'fields': 'title,year,abstract,authors.name'
}

# Directly define the API key (Reminder: Securely handle API keys in production environments)
api_key = 'api_key'  # Replace with the actual API key

# Define headers with API key
headers = {'x-api-key': api_key}

# Send the API request
response = requests.get(url, params=query_params, headers=headers)

# Check response status
if response.status_code == 200:
   response_data = response.json()
   # Process and print the response data as needed
   pretty_json = json.dumps(response_data['data'], indent=4)
   #print(pretty_json)
   #print(response_data)

   # Conexão com a base Mongo
   client = MongoClient('mongodb://s2api:S2s3m4nt1cSch*l4r@localhost:27017')
   db = client.s2api

   for s2result in response_data['data']:
      s2pretty = json.dumps(s2result, indent=4)
      print(s2pretty)
      print('**************************************************')

      db.simple_search.insert_one(s2result)

   # Encerra a conexão com a base Mongo
   client.close()
else:
   print(f"Request failed with status code {response.status_code}: {response.text}")