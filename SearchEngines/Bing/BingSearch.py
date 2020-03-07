import SearchEngines.Bing.BingAPI as BingAPI
from urllib.parse import urlparse

# Mostly for testing (not being used right now)
def get_urls(query):
    client = BingAPI.client
    web_data = client.web.search(query=query, count=33)
    urls = []
    count = 0
    for val in web_data.web_pages.value:
        count += 1
        urls.append(val.url)

    return urls

# This is the one that Infinity Search uses
def get_all(query, count=10):
    client = BingAPI.client
    web_data = client.web.search(query=query, count=count)
    data = []
    for val in web_data.web_pages.value:
        url = val.url
        parsed = urlparse(url)

        # Adding affiliate link tags
        if parsed[1] == 'www.amazon.com':
            if parsed[4] == '':
                url += '?tag=infinitysearc-20'
            if parsed[4] != '':
                url += '&tag=infinitysearc-20'

        favicon_url = 'https://' + parsed[1] + '/favicon.ico'

        data.append([val.name, url, val.snippet, favicon_url])

    return data

def get_images(query, count=10):
    # client = BingAPI.client
    # web_data = client.web.search(query=query, count=count, answer_count=count, promote=['images'], response_filter=["Images"], safe_search="Moderate")

    client = BingAPI.image_client
    image_results = client.images.search(query=query, count=count, safe_search="Moderate")

    data = []

    # if web_data.images is None:
    #     # print('None')
    #     return []
    # len(image_results.value)

    # length = len(web_data.images.value)
    length = len(image_results.value)
    index = 0

    # print(length)
    while index < length:
        image = image_results.value[index]

        width = image.width
        height = image.height

        if width > 300:
            width = width / 5
            height = height / 5

        data.append([image.thumbnail_url, image.content_url, image.host_page_url, width, height])
        index += 1

    return data


def run(query):
    # urls = get_urls(query)
    urls = get_all(query)
    # print(len(urls))
    # print(urls)


if __name__ == '__main__':
    # run('Yosemite')
    get_images('yosemite')


