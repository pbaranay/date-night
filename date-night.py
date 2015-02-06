# coding=utf-8

from flask import Flask
from flask import render_template
from flask import request
import dill
from flask_bootstrap import Bootstrap
import os
import sys
from AverageSimilarity import average_similarity

app = Flask(__name__)

svd = dill.load(open("static/svd.dill"))
# loading SVD at this point causes the intial page load to be slow,
# but others to be fast

@app.route('/')
def index():
    return render_template('bootstrap_test.html')

@app.route('/old')
def old_index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def index_post_form():
    try:
        a = request.form['yours']
        b = request.form['theirs']
    except Exception as e:
        a = None
        b = None
    d = dill.load(open("static/d.dill"))
    inv_d = dill.load(open("static/inv_d.dill"))
    try:
        id_a = inv_d[a.lower()]  # lookup_id
        id_b = inv_d[b.lower()]  # lookup_id
    except Exception as e:
        recos = ["Error - Sorry! Please try again. (Error finding movie ID's.)"]

    try:
#        svd = dill.load(open("static/svd.dill"))
        # one option would be to load svd here, but this is repetitive
        # and unnecessary, and results in long loads for EACH query
        recos = average_similarity(id_a, id_b, svd)
    except Exception as e:
        recos = ["Error -- issue loading objects."]
#         # TODO: add nicer error page
    return render_template('bootstrap_recommendations.html', yours=a, theirs=b, recos=recos[0:5])

@app.route('/about')
def about():
    return render_template('bootstrap_about.html')

@app.route('/about/1')
def slides():
    return render_template('bootstrap_about_1.html')    

@app.route('/about/2')
def about_two():
    try:
        return render_template('bootstrap_about_2.html')
    except Exception as e:
        print >> sys.stderr, e 

@app.route('/about/3')
def about_three():
    return render_template('bootstrap_about_3.html')

@app.route('/about/4')
def about_four():
    return render_template('bootstrap_about_4.html')

@app.route('/typeahead')
def typeahead():
    return render_template('the-basics.html')

if __name__ == '__main__':
    Bootstrap(app)
    app.run(host='0.0.0.0', debug=True)
