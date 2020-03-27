from flask import Flask, Blueprint, render_template, request, make_response, redirect, url_for
from MainApplication.Aggregator import CombineResults as Searches
import SearchEngines.DuckDuckGo.InstantAnswersAPI as DDG_IA
import MainApplication.Aggregator.external_links as Externals
from exchange_dict import exchange_dict
import random
import SearchEngines.Dictionary.Dictionary as Dictionary_API
import MainApplication.ddos_protection as ddos_protection
import integrations.maps.mapbox.get_coords as map_api
import MainApplication.QueryAnalyzer as QueryAnalyzer
import integrations.weather.openweather.OpenWeather as weather_api
import SearchEngines.InfinityNews.InfinityNews as InfinityNews
import SearchEngines.Invidious.Invidious as Invidious
from SearchEngines.WikiMedia.WikiSearches import wikivoyage_search

ads = [
    # ['Apple AirPods with Charging Case (Latest Model)', 'https://amzn.to/30EEOEJ', 'https://amzn.to/30EEOEJ'],
    ['Fire TV Stick 4K streaming device with Alexa built in, Ultra HD, Dolby Vision, includes the Alexa Voice Remote', 'https://amzn.to/2RaGQcC', 'https://amzn.to/2RaGQcC'],
    # ['Introducing New World, an all-new MMO from Amazon Games', 'https://amzn.to/2NLJGTb', 'https://amzn.to/2NLJGTb'],
    ['Try Twitch Prime','https://amzn.to/30DuzRb', 'https://amzn.to/30DuzRb'],
    # ['Shop Amazon Basics - HDMI Cables', 'https://amzn.to/2vap68L', 'https://amzn.to/2vap68L'],
    ['Shop Amazon - Top Rated Products', 'https://amzn.to/2sF68Ge', 'https://amzn.to/2sF68Ge'],
    ['Shop Amazon - Most Wished For Items', 'https://amzn.to/2tFEmdl', 'https://amzn.to/2tFEmdl'],
    ['Shop Amazon - Top Gift Ideas', 'https://amzn.to/2G5M9ng', 'https://amzn.to/2G5M9ng'],
    ['Shop Amazon - Hot New Releases - Updated Every Hour','https://amzn.to/37bQCkc', 'https://amzn.to/37bQCkc'],
    ['Shop Amazon - Hot New Releases - Updated Every Hour', 'https://amzn.to/37bQCkc', 'https://amzn.to/37bQCkc'],
    ['Shop Amazon - Best Selling Products - Updated Every Hour', 'https://amzn.to/3axWRBc', 'https://amzn.to/3axWRBc'],
    ['Shop Amazon Gold Box - New Deals. Everyday','https://amzn.to/30DZb4Z', 'https://amzn.to/30DZb4Z'],

    ['Shop Ebay - Electronics', 'http://rover.ebay.com/rover/1/711-53200-19255-0/1?ff3=4&pub=5575565606&toolid=10001&campid=5338647782&customid=5338647782&mpre=https%3A%2F%2Fwww.ebay.com%2Fb%2FElectronics%2Fbn_7000259124', 'https://www.ebay.com/b/Electronics/bn_7000259124'],
    ['Shop Ebay - Daily Deals', 'http://rover.ebay.com/rover/1/711-53200-19255-0/1?ff3=4&pub=5575565606&toolid=10001&campid=5338647782&customid=5338647782&mpre=https%3A%2F%2Fwww.ebay.com%2Fdeals', 'https://www.ebay.com/deals'],
    # ['Shop Ebay - Radar Detectors', 'http://rover.ebay.com/rover/1/711-53200-19255-0/1?ff3=4&pub=5575565606&toolid=10001&campid=5338647782&customid=5338647782&mpre=https%3A%2F%2Fwww.ebay.com%2Fsch%2Fi.html%3F_from%3DR40%26_trksid%3Dp2499334.m570.l1311.R1.TR12.TRC2.A0.H0.Xradar.TRS0%26_nkw%3Dradar%2Bdetectors%26_sacat%3D0', 'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2499334.m570.l1311.R1.TR12.TRC2.A0.H0.Xradar.TRS0&_nkw=radar+detectors&_sacat=0'],

    ['Fathom Analytics - Privacy-focused website analytics', 'https://usefathom.com/ref/PDKRHE', 'https://usefathom.com/ref/PDKRHE', 'This is an affiliate link provided by Infinity Search.'],

    # Sponsored Ads
    ['Simple Login - Open source email alias solution to protect your mailbox', 'https://simplelogin.io', 'https://simplelogin.io', 'Simple Login is a partner of Infinity Search that is working to restore privacy on the internet.']
]


publicAPI = Blueprint('publicAPI', __name__)
descriptions = ['Search better.', 'This search engine doesn\'t track you.', 'Made for everyone.', 'Search smarter.']

dropdown = [
    ['mojeek', 'Mojeek European Search'],
    ['shopping', 'Shopping (Coming Soon)'],
    ['wiki', 'Wiki Search']
    # Coming soon
    # ['code', 'Code (Coming Soon)'],
    # ['datasets', 'Datasets (Coming Soon)'],
    # ['research', 'Research (Coming Soon)'],
]


def get_results(query, page_number=1):
    if ddos_protection.ddos_safe() is False:
        return render_template('v2/500_traffic.html')

    words = query
    words = str(words).split()
    words_in_search = len(words)

    if words_in_search == 0:
        return redirect('/')


    ddg_ia_result = []
    if page_number == 1:
        ddg_ia_result = DDG_IA.search_ddg_ia(query)

    results = Searches.search_all(query, offset=page_number)
    external_links = Externals.get_external_links(query)

    ads_length_index = len(ads) - 1
    top_ad = ads[random.randint(0, ads_length_index)]
    bottom_ad = ads[random.randint(0, ads_length_index)]

    stock_searched = False
    stock = ''

    symbol = ''
    url = ''

    definition = []


    stock_news = False
    crypto_news = False

    weather = []
    travel = []
    map_location = []
    calculation=[]

    try:
        integrations = QueryAnalyzer.analyze_query_v2(query)
    except Exception:
        integrations = '', ''

    # if integrations[0] == 'weather':
    #     weather = weather_api.get_current_weather(integrations[1])

    if integrations[0] == 'travel':
        location = integrations[1]

    elif integrations[0] == 'maps':
        location = integrations[1]

    elif integrations[0] == 'calculator':
        calculation = [[]]

    elif integrations[0] == 'stock':
        stock_searched = True
        stock = integrations[1].upper()
        try:
            exchange = exchange_dict[stock]

        except Exception:
            exchange = 'NASDAQ'

        symbol = exchange.upper() + ':' + stock
        url = 'https://www.tradingview.com/symbols/' + exchange + '-' + stock + '/'

    elif integrations[0] == 'crypto':
        crypto_news = True

    elif integrations[0] == 'stock news':
        stock_news = True

    elif integrations[0] == 'definition':
        word_definition = Dictionary_API.search_word(words[1])
        definition = word_definition

    # return render_template('results/results.html', query=query, stock=stock, stock_searched=stock_searched,
    #                        symbol=symbol, url=url, stock_news=stock_news, crypto_news=crypto_news,
    #                        ddg_ia_result=ddg_ia_result, bing_results=results[0],
    #                        external_results=external_links, definition=definition,
    #                        top_ad=top_ad, bottom_ad=bottom_ad, current='', dropdown=dropdown, calculator=calculation)


    return render_template('v2/results.html', query=query, stock=stock, stock_searched=stock_searched,
                           symbol=symbol, url=url, stock_news=stock_news, crypto_news=crypto_news,
                           ddg_ia_result=ddg_ia_result, bing_results=results[0],
                           external_results=external_links, definition=definition,
                           top_ad=top_ad, bottom_ad=bottom_ad, current='web', dropdown=dropdown, calculator=calculation, page_number=page_number)



@publicAPI.route('/', methods=['GET', 'POST'])
def render_static():
    if request.method == 'POST':
        return render_results()
    else:
        try:
            if request.args.get('q') is not None:
                query = request.args.get('q')
                return redirect('/results?q=' + query)

        except Exception:
            description = descriptions[random.randint(0, len(descriptions) - 1)]
            return render_template('v2/home.html', description=description, dropdown=dropdown)

        description = descriptions[random.randint(0, len(descriptions) - 1)]

        return render_template('v2/home.html', description=description, dropdown=dropdown)


@publicAPI.route('/results', methods=['GET', 'POST'])
def render_results():

    if request.method == 'POST':
        try:  # In case someone tried to change the value of the form name
            form_results = dict(request.form)
            query = form_results['Search']

        except Exception:
            return redirect('/')

        return get_results(query)


    try:
        page_number = 1
        if request.args.get('page_number'):
            page_number = int(request.args.get('page_number'))
        if request.args.get('q') is not None:
            query = request.args.get('q')
            return get_results(query, page_number)

    except Exception:
        return redirect('/')

    else:
        return redirect('/')


@publicAPI.route('/advanced_search')
def render_advanced_search():
    return render_template('v2/advanced_search.html')


@publicAPI.route('/about')
def render_about():
    return render_template('v2/pages/about.html')


@publicAPI.route('/contact')
def render_contact():
    return render_template('v2/pages/contact.html')


@publicAPI.route('/privacy')
def render_privacy():
    return render_template('v2/pages/privacy.html')


@publicAPI.route('/pro')
def render_pro():
    return render_template('pro.html')


# Images ------------------

def get_image_results(query, page_number=1):
    if ddos_protection.ddos_safe() is False:
        return render_template('v2/500_traffic.html')

    words = query
    words = str(words).split()

    if len(words) == 0:
        return redirect('/')

    # external_links = Externals.get_external_links(query)
    external_links = Externals.get_image_links(query)

    results = Searches.search_bing_images(query, page_number)
    # print(results)
    # print(results[0])

    return render_template('v2/results.html', query=query, image_results=results[0],
                           external_results=external_links, current='images', dropdown=dropdown, page_number=page_number)


@publicAPI.route('/results/images',  methods=['GET', 'POST'])
def render_image_results():
    if request.method == 'POST':
        try:  # In case someone tried to change the value of the form name
            form_results = dict(request.form)
            query = form_results['Search']

        except Exception:
            return redirect('/')

        return get_image_results(query)

    try:
        page_number = 1
        if request.args.get('page_number'):
            page_number = int(request.args.get('page_number'))

        if request.args.get('q') is not None:
            query = request.args.get('q')
            return get_image_results(query, page_number=page_number)

    except Exception:
        return redirect('/')

    return redirect('/')


# # News Search Engine ---------------------------

def get_news_results(query):
    words = query
    words = str(words).split()

    if len(words) == 0:
        return redirect('/')

    external_links = Externals.get_news_links(query)

    results = InfinityNews.get_news(query)

    return render_template('v2/results.html', query=query, news_results=results[0],
                           external_results=external_links, current='news', dropdown=dropdown)


@publicAPI.route('/results/news',  methods=['GET', 'POST'])
def render_news_engine_results():
    # if request.method == 'POST':
    #     try:  # In case someone tried to change the value of the form name
    #         form_results = dict(request.form)
    #         query = form_results['Search']
    #
    #     except Exception:
    #         return redirect('/')
    #
    #     return get_news_results(query)
    #
    # else:
    #     return redirect('/news')

    if request.method == 'POST':
        try:  # In case someone tried to change the value of the form name
            form_results = dict(request.form)
            query = form_results['Search']

            return get_news_results(query)

            # external_links = Externals.get_news_links(query)
            # return render_template('news_results.html', query=query, bing_results=[],
            #                        external_results=external_links)

        except Exception as e:
            print(e)
            return redirect('/')

    try:
        if request.args.get('q') is not None:
            query = request.args.get('q')
            # external_links = Externals.get_video_links(query)
            return get_news_results(query)

            # return render_template('news_results.html', query=query, bing_results=[],
            #                        external_results=external_links)

    except Exception as e:
        print(e)
        return redirect('/')

    return redirect('/')


# Video  Results ------------------------
def get_video_results(query):
    results = Invidious.get_video_results(query)
    external_links = Externals.get_video_links(query)

    return render_template('v2/results.html', query=query, video_results=results,
                           external_results=external_links, current='videos', dropdown=dropdown)


@publicAPI.route('/results/videos',  methods=['GET', 'POST'])
def render_video_results():
    if request.method == 'POST':
        try:  # In case someone tried to change the value of the form name
            form_results = dict(request.form)
            query = form_results['Search']

            return get_video_results(query)

            # external_links = Externals.get_video_links(query)
            # return render_template('video_results.html', query=query, bing_results=[],
            #                        external_results=external_links, current='', dropdown=dropdown)

        except Exception as e:
            print(e)
            return redirect('/')

    try:
        if request.args.get('q') is not None:
            query = request.args.get('q')
            return get_video_results(query)
            # external_links = Externals.get_video_links(query)
            # return render_template('video_results.html', query=query, bing_results=[],
            #                        external_results=external_links, current='', dropdown=dropdown)

    except Exception as e:
        print(e)
        return redirect('/')

    return redirect('/')


@publicAPI.route('/results/shopping',  methods=['GET', 'POST'])
def render_shopping_results():
    if request.method == 'POST':
        try:  # In case someone tried to change the value of the form name
            form_results = dict(request.form)
            query = form_results['Search']

            external_links = Externals.get_shopping_links(query)
            return render_template('v2/results.html', query=query, bing_results=[],
                                   external_results=external_links, current='shopping', dropdown=dropdown)

        except Exception:
            return redirect('/')

    try:
        if request.args.get('q') is not None:
            query = request.args.get('q')
            external_links = Externals.get_shopping_links(query)
            return render_template('v2/results.html', query=query, bing_results=[],
                                   external_results=external_links, current='shopping', dropdown=dropdown)

    except Exception:
        return redirect('/')


    return redirect('/')


# Maps ------------------

def get_map_results(query):
    # if ddos_protection.ddos_safe() is False:
    #     return render_template('500_traffic.html')

    words = query
    words = str(words).split()

    if len(words) == 0:
        return redirect('/')

    external_links = Externals.get_map_links(query)

    wikivoyage = wikivoyage_search(query)

    location_info = map_api.get_location(query)

    return render_template('v2/results.html', query=query, wikivoyage=wikivoyage,
                           external_results=external_links, location_info=location_info, current='maps',
                           dropdown=dropdown)


@publicAPI.route('/results/maps',  methods=['GET', 'POST'])
def render_map_results():
    if request.method == 'POST':
        try:  # In case someone tried to change the value of the form name
            form_results = dict(request.form)
            query = form_results['Search']

        except Exception:
            return redirect('/')

        return get_map_results(query)
    try:
        if request.args.get('q') is not None:
            query = request.args.get('q')
            return get_map_results(query)

    except Exception:
        return redirect('/')

    return redirect('/')

# Mojeek Results ------------------------
def get_mojeek_results(query):
    # if ddos_protection.ddos_safe() is False:
    #     return render_template('500_traffic.html')

    external_links = Externals.get_external_links(query)

    # results = [[]]
    results = Searches.search_mojeek(query)
    print(results)

    # return render_template('results/mojeek_results.html', query=query, bing_results=results[0],
    #                        external_results=external_links, current='Mojeek',
    #                        dropdown=dropdown)
    return render_template('v2/results.html', query=query, mojeek_results=results[0],
                           external_results=external_links, current='mojeek',
                           dropdown=dropdown)

@publicAPI.route('/results/mojeek',  methods=['GET', 'POST'])
def render_mojeek_results():
    if request.method == 'POST':
        try:  # In case someone tried to change the value of the form name
            form_results = dict(request.form)
            query = form_results['Search']

        except Exception as e:
            print(e)
            return redirect('/')

        return get_mojeek_results(query)
    try:
        if request.args.get('q') is not None:
            query = request.args.get('q')
            return get_mojeek_results(query)

    except Exception as e:
        print(e)
        return redirect('/')

    return redirect('/')

# Wiki Results: ----------------------

def get_wiki_results(query):
    external_links = Externals.get_wiki_links(query)
    results = Searches.search_wiki_results(query)

    return render_template('v2/results.html', query=query,
                           external_results=external_links, current='wiki',
                           dropdown=dropdown,
                           wikipedia=results['Wikipedia'], wiktionary=results['Wiktionary'], wikiquote=results['Wikiquote'],
                           wikibooks=results['Wikibooks'], wikisource=results['Wikisource'], wikiversity=results['Wikiversity'],
                           wikispecies=results['Wikispecies'], wikidata=results['Wikidata'], wikicommons=results['Wikicommons'],
                           wikivoyage=results['Wikivoyage'], wikimeta=results['Metawiki']
                           )

@publicAPI.route('/results/wiki',  methods=['GET', 'POST'])
def render_wiki_results():
    if request.args.get('q') is not None:
        query = request.args.get('q')
        return get_wiki_results(query)

    if request.method == 'POST':
        try:  # In case someone tried to change the value of the form name
            form_results = dict(request.form)
            query = form_results['Search']

        except Exception as e:
            print(e)
            return redirect('/')

        return get_wiki_results(query)
    try:
        if request.args.get('q') is not None:
            query = request.args.get('q')
            return get_wiki_results(query)

    except Exception as e:
        print(e)
        return redirect('/')

    return redirect('/')

# @publicAPI.route('/v2/results',  methods=['GET', 'POST'])
# def render_v2_results():
#     return render_template('v2/results.html')
#
# @publicAPI.route('/v2/home',  methods=['GET', 'POST'])
# def render_v2_home():
#     return render_template('v2/home.html')
#
# @publicAPI.route('/v2/test', methods=['GET', 'POST'])
# def render_v2_test():
#     query = 'code'
#
#     words = query
#     words = str(words).split()
#     words_in_search = len(words)
#
#     if words_in_search == 0:
#         return redirect('/')
#
#     ddg_ia_result = DDG_IA.search_ddg_ia(query)
#     results = Searches.search_all(query)
#     external_links = Externals.get_external_links(query)
#
#     ads_length_index = len(ads) - 1
#     top_ad = ads[random.randint(0, ads_length_index)]
#     bottom_ad = ads[random.randint(0, ads_length_index)]
#
#     return render_template('v2/results.html', query=query,
#                            ddg_ia_result=ddg_ia_result, bing_results=results[0],
#                            external_results=external_links,
#                            top_ad=top_ad, bottom_ad=bottom_ad, current='', )

