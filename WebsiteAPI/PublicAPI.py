from flask import Flask, Blueprint, render_template, request, make_response, redirect, url_for
from MainApplication.Aggregator import CombineResults as Searches
import SearchEngines.DuckDuckGo.InstantAnswersAPI as DDG_IA
import MainApplication.Aggregator.external_links as Externals
from exchange_dict import exchange_dict
import random
import SearchEngines.Dictionary.Dictionary as Dictionary_API

ads = [
    ['Apple AirPods with Charging Case (Latest Model)', 'https://amzn.to/30EEOEJ', 'https://amzn.to/30EEOEJ'],
    ['Fire TV Stick 4K streaming device with Alexa built in, Ultra HD, Dolby Vision, includes the Alexa Voice Remote', 'https://amzn.to/2RaGQcC', 'https://amzn.to/2RaGQcC'],
    ['Introducing New World, an all-new MMO from Amazon Games', 'https://amzn.to/2NLJGTb', 'https://amzn.to/2NLJGTb'],
    ['Try Twitch Prime','https://amzn.to/30DuzRb', 'https://amzn.to/30DuzRb'],
    ['Shop Amazon Basics - HDMI Cables', 'https://amzn.to/2vap68L', 'https://amzn.to/2vap68L'],
    ['Shop Amazon - Top Rated Products', 'https://amzn.to/2sF68Ge', 'https://amzn.to/2sF68Ge'],
    ['Shop Amazon - Most Wished For Items', 'https://amzn.to/2tFEmdl', 'https://amzn.to/2tFEmdl'],
    ['Shop Amazon - Top Gift Ideas', 'https://amzn.to/2G5M9ng', 'https://amzn.to/2G5M9ng'],
    ['Shop Amazon - Hot New Releases - Updated Every Hour','https://amzn.to/37bQCkc', 'https://amzn.to/37bQCkc'],
    ['Shop Amazon - Hot New Releases - Updated Every Hour', 'https://amzn.to/37bQCkc', 'https://amzn.to/37bQCkc'],
    ['Shop Amazon - Best Selling Products - Updated Every Hour', 'https://amzn.to/3axWRBc', 'https://amzn.to/3axWRBc'],
    ['Shop Amazon Gold Box - New Deals. Everyday','https://amzn.to/30DZb4Z', 'https://amzn.to/30DZb4Z'],

    ['Shop Ebay - Electronics', 'http://rover.ebay.com/rover/1/711-53200-19255-0/1?ff3=4&pub=5575565606&toolid=10001&campid=5338647782&customid=5338647782&mpre=https%3A%2F%2Fwww.ebay.com%2Fb%2FElectronics%2Fbn_7000259124', 'https://www.ebay.com/b/Electronics/bn_7000259124'],
    ['Shop Ebay - Daily Deals', 'http://rover.ebay.com/rover/1/711-53200-19255-0/1?ff3=4&pub=5575565606&toolid=10001&campid=5338647782&customid=5338647782&mpre=https%3A%2F%2Fwww.ebay.com%2Fdeals', 'https://www.ebay.com/deals'],
    ['Shop Ebay - Radar Detectors', 'http://rover.ebay.com/rover/1/711-53200-19255-0/1?ff3=4&pub=5575565606&toolid=10001&campid=5338647782&customid=5338647782&mpre=https%3A%2F%2Fwww.ebay.com%2Fsch%2Fi.html%3F_from%3DR40%26_trksid%3Dp2499334.m570.l1311.R1.TR12.TRC2.A0.H0.Xradar.TRS0%26_nkw%3Dradar%2Bdetectors%26_sacat%3D0', 'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2499334.m570.l1311.R1.TR12.TRC2.A0.H0.Xradar.TRS0&_nkw=radar+detectors&_sacat=0'],

    ['Fathom Analytics - Privacy-focused website analytics', 'https://usefathom.com/ref/PDKRHE', 'https://usefathom.com/ref/PDKRHE']
]


publicAPI = Blueprint('publicAPI', __name__)
descriptions = ['Search better.', 'This search engine doesn\'t track you.', 'Made for everyone.', 'Search smarter.']


def get_results(query):
    stock_searched = False
    stock = ''

    symbol = ''
    url = ''

    definition = []

    words = query
    words = str(words).split()

    words_in_search = len(words)

    if words_in_search == 0:
        return redirect('/')

    ddg_ia_result = DDG_IA.search_ddg_ia(query)
    results = Searches.search_all(query)
    external_links = Externals.get_external_links(query)

    ads_length_index = len(ads) - 1
    top_ad = ads[random.randint(0, ads_length_index)]
    bottom_ad = ads[random.randint(0, ads_length_index)]

    if words_in_search == 1:
        return render_template('results.html', query=query, stock=stock,
                               stock_searched=stock_searched, symbol=symbol, url=url,
                               ddg_ia_result=ddg_ia_result, bing_results=results[0],
                               external_results=external_links, definition=definition,
                               top_ad=top_ad, bottom_ad=bottom_ad)

    if words_in_search == 2:
        if words[1].upper() == 'DEFINITION' or words[1].upper() == 'DEFINE':
            word_definition = Dictionary_API.search_word(words[0])
            definition = word_definition

        if words[0].upper() == 'DEFINITION' or words[0].upper() == 'DEFINE':
            word_definition = Dictionary_API.search_word(words[1])
            definition = word_definition


    if words[1].upper() == 'STOCK':
        stock_searched = True
        stock = words[0].upper()

        try:
            exchange = exchange_dict[stock]

        except Exception:
            exchange = 'NASDAQ'

        symbol = exchange.upper() + ':' + stock
        url = 'https://www.tradingview.com/symbols/' + exchange + '-' + stock + '/'

    stock_news = False
    if words[0].upper() == 'STOCK' and words[1].upper() == 'NEWS':
        stock_news = True

    crypto_news = False
    if words[0].upper() == 'CRYPTO':
        crypto_news = True

    return render_template('results.html', query=query, stock=stock, stock_searched=stock_searched,
                           symbol=symbol, url=url, stock_news=stock_news, crypto_news=crypto_news,
                           ddg_ia_result=ddg_ia_result, bing_results=results[0],
                           external_results=external_links, definition=definition,
                           top_ad=top_ad, bottom_ad=bottom_ad)


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
            return render_template('home.html', description=description)

        description = descriptions[random.randint(0, len(descriptions) - 1)]
        return render_template('home.html', description=description)


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
        if request.args.get('q') is not None:
            query = request.args.get('q')
            return get_results(query)

    except Exception:
        return redirect('/')

    else:
        return redirect('/')


@publicAPI.route('/about')
def render_about():
    return render_template('about.html')


@publicAPI.route('/contact')
def render_contact():
    return render_template('contact.html')


@publicAPI.route('/privacy')
def render_privacy():
    return render_template('privacy.html')


@publicAPI.route('/pro')
def render_pro():
    return render_template('pro.html')

# Second Page (showing less know results (Just for fun) (separate from our main search)

def get_secondpage_results(query):
    words = query
    words = str(words).split()

    if len(words) == 0:
        return redirect('/')

    external_links = Externals.get_external_links(query)
    results = Searches.second_page_results(query)

    return render_template('secondpage_results.html', query=query, bing_results=results[0],
                           external_results=external_links)


@publicAPI.route('/secondpage')
def render_second_page_home():
    return render_template('secondpage.html')

@publicAPI.route('/secondpage/results',  methods=['GET', 'POST'])
def render_second_page_results():
    if request.method == 'POST':
        try:  # In case someone tried to change the value of the form name
            form_results = dict(request.form)
            query = form_results['Search']

        except Exception:
            return redirect('/')

        return get_secondpage_results(query)

    else:
        return redirect('/secondpage')


# ---------------------


# Images ------------------

def get_image_results(query):
    words = query
    words = str(words).split()

    if len(words) == 0:
        return redirect('/')

    # external_links = Externals.get_external_links(query)
    external_links = Externals.get_image_links(query)

    results = Searches.search_bing_images(query)
    # print(results)
    print(results[0])

    return render_template('image_results.html', query=query, bing_results=results[0],
                           external_results=external_links)


@publicAPI.route('/images')
def render_image_search():
    return render_template('images.html')


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
        if request.args.get('q') is not None:
            query = request.args.get('q')
            return get_image_results(query)

    except Exception:
        return redirect('/')

    return redirect('/')


# # News Search Engine ---------------------------
# import SearchEngines.InfinityNews.InfinityNews as InfinityNews
#
# def get_news_results(query):
#     words = query
#     words = str(words).split()
#
#     if len(words) == 0:
#         return redirect('/')
#
#     external_links = Externals.get_external_links(query)
#
#     results = InfinityNews.get_news(query)
#
#     return render_template('news_results.html', query=query, bing_results=results[0],
#                            external_results=external_links)
#
# @publicAPI.route('/news')
# def render_news_search():
#     return render_template('news.html')
#
#
# @publicAPI.route('/news/results',  methods=['GET', 'POST'])
# def render_news_engine_results():
#     if request.method == 'POST':
#         try:  # In case someone tried to change the value of the form name
#             form_results = dict(request.form)
#             query = form_results['Search']
#
#         except Exception:
#             return redirect('/')
#
#         return get_news_results(query)
#
#     else:
#         return redirect('/news')
#
#

# Temporary until the news engine is live
@publicAPI.route('/results/news',  methods=['GET', 'POST'])
def render_news_engine_results():
    if request.method == 'POST':
        try:  # In case someone tried to change the value of the form name
            form_results = dict(request.form)
            query = form_results['Search']

            external_links = Externals.get_news_links(query)
            return render_template('news_results.html', query=query, bing_results=[],
                                   external_results=external_links)

        except Exception:
            return redirect('/')

    try:
        if request.args.get('q') is not None:
            query = request.args.get('q')
            external_links = Externals.get_news_links(query)
            return render_template('news_results.html', query=query, bing_results=[],
                                   external_results=external_links)

    except Exception:
        return redirect('/')

    return redirect('/')


@publicAPI.route('/results/videos',  methods=['GET', 'POST'])
def render_video_results():
    if request.method == 'POST':
        try:  # In case someone tried to change the value of the form name
            form_results = dict(request.form)
            query = form_results['Search']

            external_links = Externals.get_video_links(query)
            return render_template('video_results.html', query=query, bing_results=[],
                                   external_results=external_links)

        except Exception:
            return redirect('/')

    try:
        if request.args.get('q') is not None:
            query = request.args.get('q')
            external_links = Externals.get_video_links(query)
            return render_template('video_results.html', query=query, bing_results=[],
                                   external_results=external_links)

    except Exception:
        return redirect('/')

    return redirect('/')


@publicAPI.route('/results/shopping',  methods=['GET', 'POST'])
def render_shopping_results():
    if request.method == 'POST':
        try:  # In case someone tried to change the value of the form name
            form_results = dict(request.form)
            query = form_results['Search']

            external_links = Externals.get_shopping_links(query)
            return render_template('shopping_results.html', query=query, bing_results=[],
                                   external_results=external_links)

        except Exception:
            return redirect('/')

    try:
        if request.args.get('q') is not None:
            query = request.args.get('q')
            external_links = Externals.get_shopping_links(query)
            return render_template('shopping_results.html', query=query, bing_results=[],
                                   external_results=external_links)

    except Exception:
        return redirect('/')

    return redirect('/')



