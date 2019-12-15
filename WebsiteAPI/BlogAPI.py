from flask import Blueprint, render_template, jsonify, request, redirect

blogAPI = Blueprint('blogAPI', __name__)

@blogAPI.route('/content')
def render_articles():
    articles = [
        {'link': '/articles/more_about_us', 'title': 'More Privacy Information About Us'},
        {'link': '/articles/about_our_company', 'title': 'About Our Company'},
        {'link': '/articles/open_source', 'title': 'Infinity Search Is Now Open Source'},
        {'link' : '/articles/privacy_resources', 'title' : 'Privacy Resources'},
    ]

    return render_template('articles/articles.html', articles=articles)

@blogAPI.route('/articles/<post>')
def render_blog_post(post):
    try:
        return render_template('articles/' + post + '.html')
    except Exception as e:
        return redirect('/404')

