from flask import Blueprint, render_template, jsonify, request, redirect
import random

blogAPI = Blueprint('blogAPI', __name__)

# For English: ----------------------

@blogAPI.route('/content')
def render_articles():
    articles = [
        {'link': '/articles/surprise', 'title': 'Surprise Me!'},
        {'link': '/articles/languages', 'title': 'We Now Have Infinity Search In German and Spanish'},
        {'link': '/articles/secondpage', 'title': 'Why We Made Second Page'},
        {'link': '/articles/more_about_us', 'title': 'More Privacy Information About Us'},
        {'link': '/articles/about_our_company', 'title': 'About Our Company'},
        {'link': '/articles/open_source', 'title': 'Infinity Search Is Now Open Source'},
        {'link' : '/articles/privacy_resources', 'title' : 'Privacy Resources'}
    ]

    return render_template('articles/articles.html', articles=articles)


@blogAPI.route('/articles/<post>')
def render_blog_post(post):
    try:
        return render_template('articles/' + post + '.html')
    except Exception as e:
        print(e)
        return redirect('/404')


@blogAPI.route('/articles/surprise')
def render_surprise():
    surprise_searches = ['/results?q=AAPL stock', '/results/news?q=Politics', '/results/maps?q=Labrador Canada',
                         '/results/images?q=swiss alps', '/results/mojeek?q=eu', '/results/videos?q=PewDiePie',
                         '/results?q=define philosophy']
    surprise_search = surprise_searches[random.randint(0, len(surprise_searches)) - 1]

    return render_template('articles/surprise.html', surprise_search=surprise_search)


# For German: ----------------------
@blogAPI.route('/content/de')
def render_articles_german():
    articles = [
        {'link': '/articles/languages/de', 'title': 'Wir Haben Jetzt Infinity-Suche In Deutsch Und Spanisch'},
        {'link': '/articles/more_about_us/de', 'title': 'Weitere Datenschutzinformationen über uns'},
        {'link': '/articles/about_our_company/de', 'title': 'Über unser Unternehmen'},
        {'link': '/articles/open_source/de', 'title': 'Infinity Search ist jetzt Open Source'},
        {'link' : '/articles/privacy_resources/de', 'title' : 'Datenschutzressourcen'},
    ]

    return render_template('languages/german/articles/articles.html', articles=articles)

@blogAPI.route('/articles/<post>/de')
def render_blog_post_german(post):
    try:
        return render_template('languages/german/articles/' + post + '.html')
    except Exception as e:
        return redirect('/404')

# For Spanish: ----------------------
@blogAPI.route('/content/es')
def render_articles_spanish():
    articles = [
        {'link': '/articles/languages/es', 'title': 'Ahora Tenemos Infinity Search En Alemán Y Español'},
        {'link': '/articles/more_about_us/es', 'title': 'Más Información De Privacidad Sobre Nosotros'},
        {'link': '/articles/about_our_company/es', 'title': 'Acerca De Nuestra Empresa'},
        {'link': '/articles/open_source/es', 'title': 'Infinity Search Es Ahora De Código Abierto'},
        {'link' : '/articles/privacy_resources/es', 'title' : 'Recursos De Privacidad'},
    ]

    return render_template('languages/spanish/articles/articles.html', articles=articles)

@blogAPI.route('/articles/<post>/es')
def render_blog_post_spanish(post):
    try:
        return render_template('languages/spanish/articles/' + post + '.html')
    except Exception as e:
        return redirect('/404')
