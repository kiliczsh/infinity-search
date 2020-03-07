import requests
import pprint

def format_open_search_results(results):
    formatted_results = []

    titles = results[1]

    res_length = len(titles)
    count = 0
    while count < res_length:
        formatted_results.append([titles[count], results[3][count]])
        count += 1

    return formatted_results

'''
Wikipedia 
'''
def wikipedia_search(query):
    results = requests.get('https://wikipedia.org/w/api.php?action=opensearch&search=' + query + '&format=json').json()
    return format_open_search_results(results)

'''
Wiktionary
'''
def wiktionary_search(query):
    results = requests.get('https://wiktionary.org/w/api.php?action=opensearch&search=' + query + '&format=json').json()
    return format_open_search_results(results)

'''
Wikibooks
'''
def wikibooks_search(query):
    results = requests.get('https://wikibooks.org/w/api.php?action=opensearch&search=' + query + '&format=json').json()
    return format_open_search_results(results)

'''
Wikiquote
'''
def wikiquote_search(query):
    results = requests.get('https://wikiquote.org/w/api.php?action=opensearch&search=' + query + '&format=json').json()
    return format_open_search_results(results)

'''
Wikivoyage
'''
def wikivoyage_search(query):
    results = requests.get('https://wikivoyage.org/w/api.php?action=opensearch&search=' + query + '&format=json').json()
    return format_open_search_results(results)

'''
Wikisource
'''
def wikisource_search(query):
    results = requests.get('https://wikisource.org/w/api.php?action=opensearch&search=' + query + '&format=json').json()
    return format_open_search_results(results)

'''
https://commons.wikimedia.org/w/api.php?action=opensearch&search=code
'''

'''
Wikicommons
'''
def wikicommons_search(query):
    results = requests.get('https://commons.wikimedia.org/w/api.php?action=opensearch&search=' + query + '&format=json').json()
    return format_open_search_results(results)


# '''
# Media Wiki
# '''
# def mediawiki_search(query):
#     results = requests.get('https://www.mediawiki.org/w/api.php?action=opensearch&search=' + query + '&format=json').json()
#     return format_open_search_results(results)
#

'''
Wikispecies
'''
def wikispecies_search(query):
    results = requests.get('https://wikispecies.org/w/api.php?action=opensearch&search=' + query + '&format=json').json()
    return format_open_search_results(results)

'''
Wikinews
'''
def wikinews_search(query):
    results = requests.get('https://wikinews.org/w/api.php?action=opensearch&search=' + query + '&format=json').json()
    return format_open_search_results(results)

'''
Wikiversity
'''
def wikiversity_search(query):
    results = requests.get('https://wikiversity.org/w/api.php?action=opensearch&search=' + query + '&format=json').json()
    return format_open_search_results(results)

'''
Wikidata
'''
def wikidata_search(query):
    # OpenSearch does not work for wikidata
    non_open_search_endpoint = 'https://www.wikidata.org/w/api.php?action=query&list=search&srsearch='+ query +'&srlimit=10&srprop=size&formatversion=2&format=json'
    results = requests.get(non_open_search_endpoint).json()

    return results

'''
MetaWiki
'''
def meta_wiki_search(query):
    # https://meta.wikimedia.org/w/api.php

    results = requests.get('https://meta.wikimedia.org/w/api.php?action=opensearch&search=' + query).json()

    return format_open_search_results(results)


# ---------------------


def wikimedia_search_v2(query):
    # https://commons.wikimedia.org/w/api.php

    results = requests.get('https://commons.wikimedia.org/w/api.php?action=opensearch&search=' + query).json()
    print(results)
    pprint.pprint(results)


def parse_wiktionary_search(url):
    wikipage = requests.get(url).text

    print(wikipage)
    # TODO: Parse the page to find the type, definition, sentence, usage, and root


def wiktionary_search_direct_hit(query):
    # https://commons.wikimedia.org/w/api.php

    # https://en.wiktionary.org/w/api.php?action=query&titles=test&format=json

    results = requests.get('https://en.wiktionary.org/w/api.php?action=query&format=json&titles=' + query).json()
    print(results)
    # pprint.pprint(results)

    result_date = results['query']['pages']
    page_number = list(result_date.keys())[0]

    if page_number == '-1':
        print('No results')
        return []

    # print(page_number)

    wikipage_url = 'https://en.wiktionary.org/?curid=' + page_number

    print(wikipage_url)

    return [wikipage_url]




# -------------

def get_wikipedia_page_from_id(page_id):
    # 'http://en.wikipedia.org/?curid=18630637'

    results = requests.get('http://en.wikipedia.org/?curid=' + page_id).text
    print(results)
    # pprint.pprint(results)


def get_wikipedia_general_info(query):
    # https://en.wikipedia.org/w/api.php?action=query&formatversion=2&prop=extracts%7Cpageimages%7Crevisions&titles=Albert+Einstein&redirects=&exintro=true&exsentences=2&explaintext=true&piprop=thumbnail&pithumbsize=300&rvprop=timestamp&format=json

    results = requests.get('https://en.wikipedia.org/w/api.php?action=query&formatversion=2&prop=extracts%7Cpageimages%7Crevisions&titles=' + query + '&redirects=&exintro=true&exsentences=2&explaintext=true&piprop=thumbnail&pithumbsize=300&rvprop=timestamp&format=json').json()
    print(results)
    pprint.pprint(results)


def get_wikipedia_search_results(query):
    query = query.replace(' ', '+')
    endpoint = 'https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=morelike:Marie_Curie%7Cradium&srlimit=10&srprop=size&formatversion=2'
    endpoint = 'https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=morelike:'+ query +'&srlimit=10&srprop=size&formatversion=2&format=json'
    endpoint = 'https://wikipedia.org/w/api.php?action=query&list=search&srsearch='+ query +'&srlimit=10&srprop=size&formatversion=2&format=json'

    results = requests.get(endpoint).json()

    # print(results)
    # pprint.pprint(results.json())

    return results


def find_something_obscure_wikipedia_cirrus(query):
    # https://www.mediawiki.org/wiki/API:Search_and_discovery
    endpoint = 'https://en.wikipedia.org/w/index.php?title=Special:Search&cirrusDumpResult=&search=napolean+dog'
    endpoint = 'https://en.wikipedia.org/w/index.php?title=Special:Search&cirrusDumpResult=&search=' + query

    # TODO: Check if query is actually obscure enough and that the page does not redirect to one that already exists
    results = requests.get(endpoint)
    print(results)
    pprint.pprint(results.json())


# ---------

def wikivoyage_search_v2(query):
    endpoint = 'https://en.wikivoyage.org/w/api.php?action=query&list=search&srsearch=Panama&srlimit=10&srprop=size&formatversion=2&format=json'
    results = requests.get(endpoint).json()
    # print(results)
    # pprint.pprint(results.json())

    return results

def wikivoyage_similar_results(query):
    endpoint = 'https://en.wikivoyage.org/w/api.php?action=query&list=search&srsearch=morelike:Panama|radium&srlimit=10&srprop=size&formatversion=2'


def get_all_results_v2(query):
    results = {}

    formatted_wikipedia = []
    wikipedia_results = get_wikipedia_search_results(query)['query']['search']
    print(wikipedia_results)
    for result in wikipedia_results:
        formatted_wikipedia.append([result['title'], 'https://en.wikipedia.org/wiki/?curid=' + str(result['pageid'])])
    results['Wikipedia'] = formatted_wikipedia

    formatted_wikivoyage = []
    wikivoyage_results = wikivoyage_search(query)['query']['search']
    print(wikivoyage_results)
    for result in wikivoyage_results:
        formatted_wikipedia.append([result['title'], 'https://en.wikivoyage.org/wiki/?curid=' + str(result['pageid'])])
    results['Wikivoyage'] = formatted_wikipedia

    print(results)

    return results


def get_all_results_open_search(query):
    results = {
        'Wikipedia' : wikipedia_search(query),
        'Wiktionary': wiktionary_search(query),
        'Wikibooks': wikibooks_search(query),
        'Wikiquote': wikiquote_search(query),
        'Wikivoyage': wikivoyage_search(query),
        'Wikisource': wikisource_search(query),
        'Wikispecies': wikispecies_search(query),
        'Wikinews': wikinews_search(query),
        'Wikiversity': wikiversity_search(query),
        # 'Wikidata': wikidata_search(query),
        'Metawiki' : meta_wiki_search(query),
        'Wikicommons' : wikicommons_search(query)
    }

    return results

