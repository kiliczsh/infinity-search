import requests
from pprint import pprint
from urllib.parse import urlparse
from accounts import mojeek_api_key

def get_results(query, s=None):

    if s is None:
        search_request_json = requests.get('https://www.mojeek.com/search?api_key='+ mojeek_api_key +'&fmt=json&q=' + query).json()
    else:
        search_request_json = requests.get('https://www.mojeek.com/search?api_key='+ mojeek_api_key +'&s=' + str(s) +'&fmt=json&q=' + query).json()

    response = search_request_json['response']

    if response['status'] != 'OK':
        return False  # If this happens we display bing results

    formatted_results = []

    results = response['results']

    for result in results:
        parsed = urlparse(result['url'])

        # if parsed[0] == 'http':
        #     result['url'] = result['url'].replace('http://', 'https://')  # Force https

        favicon_url = 'https://' + parsed[1] + '/favicon.ico'

        formatted_results.append([result['title'], result['url'], result['desc'], favicon_url])

    return formatted_results





if __name__ == '__main__':
    res = get_results('Mojeek')
    print(res)
