import requests
from urllib.parse import urlparse
from math import floor
import datetime as dt
from accounts import news_endpoint

def read_date(date):
    # Note: This date reader is not pretty, but it works for now
    current_time = dt.datetime.now() + dt.timedelta(hours=6)
    parsed_date = date.split('T')

    split_date = parsed_date[0].split('-')
    year = split_date[0]
    month = split_date[1]
    day = split_date[2]

    # Option 1
    try:
        split_day = parsed_date[1].split("-")
        hour_difference = split_day[1].split(':')
        hour_split = split_day[0].split(':')

        # print(hour_split)
        hour = hour_split[0]
        minute = hour_split[1]
        second = hour_split[2]

        date = dt.datetime(year=int(year), month=int(month), day=int(day), hour=int(hour), minute=int(minute), second=int(second)) + dt.timedelta(hours=int(hour_difference[0]), minutes=int(hour_difference[1]))

        # print(date)
        minutes_difference = (current_time - date).total_seconds() / 60.0
        return minutes_difference, minutes_difference / 60

    except Exception as e:
        # print(e)
        x = 0

    # Option 2
    try:
        split_day = parsed_date[1].split("+")
        hour_difference = split_day[1].split(':')
        hour_split = split_day[0].split(':')

        # print(hour_split)
        hour = hour_split[0]
        minute = hour_split[1]
        second = hour_split[2]

        date = dt.datetime(year=int(year), month=int(month), day=int(day), hour=int(hour), minute=int(minute), second=int(second)) - dt.timedelta(hours=int(hour_difference[0]), minutes=int(hour_difference[1]))

        minutes_difference = (current_time - date).total_seconds() / 60.0
        return minutes_difference, minutes_difference / 60

    except Exception as e:
        x = 0

    # Option 3
    try:
        split_day = parsed_date[1].split("Z")
        hour_difference = split_day[1].split(':')

        hour_split = split_day[0].split(':')

        hour = hour_split[0]
        minute = hour_split[1]
        second = hour_split[2]

        date = dt.datetime(year=int(year), month=int(month), day=int(day), hour=int(hour), minute=int(minute), second=int(second))

        minutes_difference = (current_time - date).total_seconds() / 60.0
        return minutes_difference, minutes_difference / 60

    except Exception as e:
        x = 0

    return -1, -1





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


    for result in results:

        source = result['_source']

        # print(source)
        date = read_date(source['page_date'])
        # print(date)
        # print(source['title'])

        parsed = urlparse(source['url'])

        if parsed[0] == 'http':
            source['url'] = source['url'].replace('http://', 'https://')  # Force https

        favicon_url = 'https://' + parsed[1] + '/favicon.ico'

        minutes_ago = source['minutes_ago']
        hours_ago = source['hours_ago']

        # links.append([source['title'] ,source['url'], round(minutes_ago), favicon_url, floor(hours_ago)])
        links.append([source['title'] ,source['url'], round(date[0]), favicon_url, floor(date[1])])



    # print(links)

    all_results = []
    all_results = combine_results(all_results, links)
    # ranked_results = rank_all(all_results)
    return all_results

    # return links


if __name__ == '__main__':
    get_news('Code')


