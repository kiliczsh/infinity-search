from flask import Flask, Blueprint, render_template, request, make_response, redirect, url_for
from MainApplication.Aggregator import CombineResults as Searches
import SearchEngines.DuckDuckGo.InstantAnswersAPI as DDG_IA
import MainApplication.Aggregator.external_links as Externals
from exchange_dict import exchange_dict
import random

spanishAPI = Blueprint('spanishAPI', __name__)
descriptions = ['Busca mejor.', 'Este motor de búsqueda no te rastrea.', 'Hecho para todos.',
                'Busque más inteligentemente.']


def get_results(query):
    search_ddg_ia = True
    ddg_ia_cb = 'checked'
    search_bing = True
    bing_cb = 'checked'

    stock_searched = False
    stock = ''

    symbol = ''
    url = ''

    words = query
    words = str(words).split()

    if len(words) == 0:
        return redirect('/es')

    if len(words) == 1:
        results = Searches.search_all(query)
        ddg_ia_result = []
        if search_ddg_ia is True:
            ddg_ia_result = DDG_IA.search_ddg_ia(query)
        external_links = Externals.get_external_links_spanish(query)

        return render_template('languages/spanish/results.html', query=query, stock=stock,
                               stock_searched=stock_searched, symbol=symbol, url=url, bing_cb=bing_cb,
                               ddg_ia_cb=ddg_ia_cb,
                               ddg_ia_result=ddg_ia_result, bing_results=results[0],
                               external_results=external_links)

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

    results = Searches.search_all(query)

    ddg_ia_result = []
    if search_ddg_ia is True:
        ddg_ia_result = DDG_IA.search_ddg_ia(query)

    external_links = Externals.get_external_links_spanish(query)

    return render_template('languages/spanish/results.html', query=query, stock=stock, stock_searched=stock_searched,
                           symbol=symbol, url=url, stock_news=stock_news, crypto_news=crypto_news, bing_cb=bing_cb,
                           ddg_ia_cb=ddg_ia_cb,
                           ddg_ia_result=ddg_ia_result, bing_results=results[0],
                           external_results=external_links)


@spanishAPI.route('/es', methods=['GET', 'POST'])
def render_static():
    if request.method == 'POST':
        return render_results()
    else:
        try:
            if request.args.get('q') is not None:
                query = request.args.get('q')
                return get_results(query)

        except Exception:

            description = descriptions[random.randint(0, len(descriptions) - 1)]
            return render_template('languages/spanish/home.html', description=description)

        description = descriptions[random.randint(0, len(descriptions) - 1)]
        return render_template('languages/spanish/home.html', description=description)


@spanishAPI.route('/results/es', methods=['GET', 'POST'])
def render_results():
    if request.method == 'POST':
        try:  # In case someone tried to change the value of the form name
            form_results = dict(request.form)
            query = form_results['Search']

        except Exception:
            return redirect('/es')

        return get_results(query)

    else:
        return redirect('/es')


@spanishAPI.route('/about/es')
def render_about():
    return render_template('languages/spanish/about.html')


@spanishAPI.route('/contact/es')
def render_contact():
    return render_template('languages/spanish/contact.html')


@spanishAPI.route('/privacy/es')
def render_privacy():
    return render_template('languages/spanish/privacy.html')

@spanishAPI.route('/pro/es')
def render_pro():
    return render_template('languages/spanish/pro.html')

