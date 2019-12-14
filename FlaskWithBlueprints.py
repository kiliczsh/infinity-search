from flask import Flask, render_template, request, flash, session, redirect, url_for, send_from_directory
import os

# Blueprints
from WebsiteAPI.PublicAPI import publicAPI
from WebsiteAPI.BlogAPI import blogAPI

app = Flask(__name__)

app.register_blueprint(publicAPI)
app.register_blueprint(blogAPI)


# app.jinja_env.cache = {} # Apparently this line of code can decrease response time if the cache is too large

@app.before_request
def before_request():
    # This is just so that we do not force https when testing the site on localhost
    if request.url.startswith('http://localhost') or request.url.startswith(
            'http://127.0.0.1'):  # If it is being ran locally
        return

    # Auto redirect to https
    if request.url.startswith('http://'):
        url = request.url.replace('http://', 'https://', 1)
        code = 301
        return redirect(url, code=code)

    return


@app.route('/robots.txt')
def render_robots():
    return send_from_directory(app.static_folder, 'robots.txt')


# @app.route('/favicon.ico')
# def favicon():
#     return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html')


if __name__ == '__main__':
    app.run()
