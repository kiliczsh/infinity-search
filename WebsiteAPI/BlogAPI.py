from flask import Blueprint, render_template, jsonify, request, redirect
import random

blogAPI = Blueprint('blogAPI', __name__)

@blogAPI.route('/blog')
def render_blog():
    articles = [
        # {'link': '/blog/press', 'title': 'Infinity Search Press Coverage'},
        {'link': '/blog/privacy_browser_extensions', 'title': 'Privacy Browser Extensions'},
        {'link': '/blog/surprise', 'title': 'Surprise Me!'},
        # {'link': '/blog/languages', 'title': 'We Now Have Infinity Search In German and Spanish'},
        {'link': '/blog/more_about_us', 'title': 'More Privacy Information About Us'},
        {'link': '/blog/about_our_company', 'title': 'About Our Company'},
        {'link': '/blog/open_source', 'title': 'Infinity Search Is Now Open Source'},
        {'link' : '/blog/privacy_resources', 'title' : 'Privacy Resources'}
    ]

    return render_template('v2/pages/blog/articles.html', articles=articles)


@blogAPI.route('/blog/<post>')
def render_blog_post(post):
    try:
        return render_template('v2/pages/blog/' + post + '.html')
    except Exception as e:
        print(e)
        return redirect('/404')


@blogAPI.route('/ad/<ad_id>')
def ad_redirect(ad_id):

    ad_dict = {
        'abc' : 'ad_url'
    }

    if ad_id in ad_dict:
        # Count the click rate
        print(ad_dict[ad_id])
        return redirect(ad_dict[ad_id])

    return redirect('/')


@blogAPI.route('/blog/surprise')
def render_surprise():
    surprise_searches = ['/results?q=AAPL stock', '/results/news?q=Politics', '/results/maps?q=Labrador Canada',
                         '/results/images?q=swiss alps', '/results/mojeek?q=eu', '/results/videos?q=PewDiePie',
                         '/results?q=define philosophy', '/results?q=stock news', '/results?q=crypto news'
                         ]

    surprise_search = surprise_searches[random.randint(0, len(surprise_searches)) - 1]

    return render_template('v2/pages/blog/surprise.html', surprise_search=surprise_search)


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
