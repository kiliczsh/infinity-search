from flask import Flask, Blueprint, render_template, request, make_response, redirect, url_for

designsAPI = Blueprint('designsAPI', __name__)

# Just for testing different color schemes and designs for the website

#
# @designsAPI.route('/designs/one/home')
# def render_d1_home():
#     return render_template('designs/one/home1.html')
#
# @designsAPI.route('/designs/one/results')
# def render_d1_results():
#     return render_template('designs/one/results1.html')
#
