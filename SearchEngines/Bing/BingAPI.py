# Import required modules.
from azure.cognitiveservices.search.websearch import WebSearchAPI
from azure.cognitiveservices.search.websearch.models import SafeSearch
from msrest.authentication import CognitiveServicesCredentials

# Just variables in the accounts.py files that is gitignored
from accounts import subscription_key, endpoint

# Instantiate the client and replace with your endpoint.
client = WebSearchAPI(CognitiveServicesCredentials(subscription_key), base_url = endpoint)

def get_web_pages(query):
    web_data = client.web.search(query=query)
    return web_data.web_pages

