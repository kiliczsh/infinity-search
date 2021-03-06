import SearchEngines.Bing.BingSearch as Bing
import SearchEngines.Mojeek.MojeekSearch as Mojeek
import SearchEngines.WikiMedia.WikiSearches as WikiMedia

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

    # for page in data:
    #     x = 0

    data.append(['View More Results From Bing', 'https://www.bing.com/search?q=' + formatted_query, '', 'https://www.bing.com/favicon.ico'])

    return data

def format_mojeek(data):
    # Mojeek Data is already formatted
    data.append(['View More Results From Mojeek', 'https://www.mojeek.com/search?&q=' + formatted_query, '', 'https://www.mojeek.com/favicon.ico'])

    return data

# really just Bing for now
def search_all(query, offset=0):
    format_query(query)

    # try:
    #     mojeek1 = Mojeek.get_results(formatted_query)
    #     mojeek2 = Mojeek.get_results(formatted_query, s=11)
    #
    #     # print(mojeek1)
    #     # print(mojeek2)
    #
    #     mojeek = mojeek1
    #     for page in mojeek2:
    #         mojeek.append(page)
    #
    #     mojeek = format_mojeek(mojeek)
    #
    #     all_results = []
    #     all_results = combine_results(all_results, mojeek)
    #     ranked_results = rank_all(all_results)
    #     return ranked_results
    #
    # except Exception as e:
    #     print(e)
    #     mojeek = [[]]

    try:
        bing = Bing.get_all(query, count=25, offset=offset)
    except Exception as e:
        # print(e)
        bing = [[]]

    bing = format_bing(bing)
    all_results = []
    all_results = combine_results(all_results, bing)
    ranked_results = rank_all(all_results)
    return ranked_results


def search_mojeek(query):
    format_query(query)

    try:
        mojeek1 = Mojeek.get_results(formatted_query)
        mojeek2 = Mojeek.get_results(formatted_query, s=11)

        # print(mojeek1)
        # print(mojeek2)

        mojeek = mojeek1
        for page in mojeek2:
            mojeek.append(page)

        mojeek = format_mojeek(mojeek)

        all_results = []
        all_results = combine_results(all_results, mojeek)
        ranked_results = rank_all(all_results)
        return ranked_results

    except Exception as e:
        print(e)
        # mojeek = [[]]
        return [[]]

    # mojeek = format_bing(mojeek)
    # all_results = []
    # all_results = combine_results(all_results, mojeek)
    # ranked_results = rank_all(all_results)
    # return ranked_results

def search_bing_images(query, offset=1):
    try:
        bing = Bing.get_images(query, count=10, offset=offset)
    except Exception as e:
        print(e)
        return [[]]
        # bing = []

    # bing = format_bing(bing)
    all_results = []
    all_results = combine_results(all_results, bing)
    ranked_results = rank_all(all_results)
    return ranked_results


def search_bing_mojeek(query):
    try:
        mojeek = Mojeek.get_results(formatted_query)
        bing = Bing.get_all(formatted_query)

        for result in bing:
            count = 0
            for res in mojeek:
                count += 1
                if result[1] == res[1]:
                    print('F')

    except Exception as e:
        print(e)
        results =[[]]

    # print('')


def second_page_results(query): # From Mojeek
    format_query(query)

    try:
        mojeek = Mojeek.get_results(formatted_query, s=21)
        mojeek = format_mojeek(mojeek)
        all_results = []
        all_results = combine_results(all_results, mojeek)
        ranked_results = rank_all(all_results)
        return ranked_results

    except Exception as e:
        print(e)
        mojeek = [[]]

    mojeek = format_mojeek(mojeek)
    all_results = []
    all_results = combine_results(all_results, mojeek)
    ranked_results = rank_all(all_results)
    return ranked_results



def search_wiki_results(query):
    format_query(query)
    try:
        results = WikiMedia.get_all_results_open_search(query)
        results['Wikidata'] = []

    except Exception as e:
        print(e)
        results = {'Wikipedia': [], 'Wiktionary': [], 'Wikibooks': [], 'Wikiquote': [], 'Wikivoyage': [],
                   'Wikisource': [], 'Wikispecies': [], 'Wikinews': [], 'Wikiversity': [], 'Wikidata': [],
                   'Metawiki': [], 'Wikicommons': []
                   }

    return results





