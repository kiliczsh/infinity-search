import SearchEngines.Bing.BingAPI as BingAPI

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
        data.append([val.name,val.url, val.snippet])

    return data

def run(query):
    # urls = get_urls(query)
    urls = get_all(query)
    # print(len(urls))
    # print(urls)


if __name__ == '__main__':
    run('Yosemite')


