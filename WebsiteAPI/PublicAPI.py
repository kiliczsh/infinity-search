from flask import Flask, Blueprint, render_template, request, make_response, redirect, url_for
from MainApplication.Aggregator import CombineResults as Searches
import SearchEngines.DuckDuckGo.InstantAnswersAPI as DDG_IA
import MainApplication.Aggregator.external_links as Externals
from exchange_dict import exchange_dict
import random
import SearchEngines.Dictionary.Dictionary as Dictionary_API


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


    if words_in_search == 1:
        return render_template('results.html', query=query, stock=stock,
                               stock_searched=stock_searched, symbol=symbol, url=url,
                               ddg_ia_result=ddg_ia_result, bing_results=results[0],
                               external_results=external_links, definition=definition)

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
                           external_results=external_links, definition=definition)


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

# def get_image_results(query):
#     words = query
#     words = str(words).split()
#
#     if len(words) == 0:
#         return redirect('/')
#
#     external_links = Externals.get_external_links(query)
#
#     results = Searches.search_bing_images(query)
#     print(results)
#
#     return render_template('image_results.html', query=query, bing_results=results[0],
#                            external_results=external_links)
#
#
# @publicAPI.route('/images')
# def render_image_search():
#     return render_template('images.html')
#

# @publicAPI.route('/images/results',  methods=['GET', 'POST'])
# def render_image_results():
#     if request.method == 'POST':
#         try:  # In case someone tried to change the value of the form name
#             form_results = dict(request.form)
#             query = form_results['Search']
#
#         except Exception:
#             return redirect('/')
#
#         return get_image_results(query)
#
#     else:
#         return redirect('/news')


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
