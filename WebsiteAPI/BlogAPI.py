from flask import Blueprint, render_template, jsonify, request

blogAPI = Blueprint('blogAPI', __name__)

@blogAPI.route('/content')
def render_articles():
    articles = [
        {'link' : '/articles/resources', 'title' : 'Privacy Resources'},
        {'link' : '/articles/hello_world', 'title' : 'Our First Blog Post'}
        ]

    return render_template('articles/articles.html', articles=articles)

@blogAPI.route('/articles/resources')
def render_blog_privacy_resources():
    return render_template('articles/Privacy_Resources.html')

@blogAPI.route('/articles/hello_world')
def render_blog_hello_world():
    return render_template('articles/hello_world.html')
