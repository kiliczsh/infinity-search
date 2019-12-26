import requests
from pprint import pprint

def search_ddg_ia(search):
    try:
        query = search.replace(' ', '+')
        instant_answer = requests.get('https://api.duckduckgo.com/?q='+ query + '&format=json').json()
        # pprint(instant_answer)

        if instant_answer['AbstractSource'] == '': # If there is nothing to display
            return []

        if instant_answer['AbstractText'] == '': # If we need to check for related topics because there is no direct one

            if len(instant_answer['RelatedTopics']) > 0: # If there is a related topic
                heading = instant_answer['Heading']
                description = instant_answer['RelatedTopics'][0]['Text']
                url = instant_answer['AbstractURL']
                image_url = instant_answer['RelatedTopics'][0]['Icon']['URL']

                return [[heading, description, url, image_url]]

            else: # If there is nothing to display
                return []

        else: # If there are new abstract texts
            return [[instant_answer['Heading'], instant_answer['AbstractText'], instant_answer['AbstractURL'], instant_answer['Image']]]

    except Exception:
        return []

def run(query):
    query = query.replace(' ', '+')
    results = requests.get('https://api.duckduckgo.com/?q='+ query + '&format=json').json()
    pprint(results)

    return results


if __name__ == '__main__':
    # run('Old navy')
    d = search_ddg_ia('Denmark')

