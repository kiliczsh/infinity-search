import SearchEngines.Bing.BingSearch as Bing

formatted_query = ''


# Just making the query in the form of a query string by replacing the spaces with a '+'
def format_query(query):
    global formatted_query
    formatted_query = query.replace(' ', '+')


# Coming later
def rank_all(results):
    # print(len(results))
    return results


def combine_results(current, new):
    all_data = current
    # for page in new:
    #     all_data.append(page)
    all_data.append(new)

    return all_data


def format_bing(data):
    # Bing Data is already formatted

    for page in data:
        x = 0

    data.append(['View More Results From Bing', 'https://www.bing.com/search?q=' + formatted_query, '', 'www.bing.com/favicon.ico'])

    return data


def search_all(query, bing_search):
    format_query(query)

    try:
        bing = Bing.get_all(query, count=25)
    except Exception as e:
        print(e)
        bing = [[]]

    bing = format_bing(bing)
    all_results = []
    all_results = combine_results(all_results, bing)
    ranked_results = rank_all(all_results)
    return ranked_results

# if __name__ == '__main__':
    # x = search_all('Python')
    #
    # for l in x:
    #     print(l)


