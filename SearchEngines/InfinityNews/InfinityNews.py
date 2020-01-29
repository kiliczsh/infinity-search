import requests
from urllib.parse import urlparse
from math import floor

from accounts import news_endpoint

def combine_results(current, new):
    all_data = current
    # for page in new:
    #     all_data.append(page)
    all_data.append(new)

    return all_data


def get_news(query):

    links = []

    query = query.replace(' ', '+')

    # data = requests.get('http://localhost:9200/news_engine/_search?q=' + query + '&size=' + str(20) + '&pretty=true').json()
    data = requests.get(news_endpoint + '/news_engine/_search?q=' + query + '&size=' + str(20) + '&pretty=true').json()

    # print(data)

    results = data['hits']['hits']

    for noticia in results:
        # print(noticia)

        source = noticia['_source']

        # print(source)
        # print(source['title'])

        parsed = urlparse(source['url'])

        if parsed[0] == 'http':
            source['url'] = source['url'].replace('http://', 'https://')  # Force https

        favicon_url = 'https://' + parsed[1] + '/favicon.ico'

        minutes_ago = source['minutes_ago']
        hours_ago = source['hours_ago']

        links.append([source['title'] ,source['url'], round(minutes_ago), favicon_url, floor(hours_ago)])


    # print(links)

    all_results = []
    all_results = combine_results(all_results, links)
    # ranked_results = rank_all(all_results)
    return all_results

    # return links


if __name__ == '__main__':
    get_news('Code')


