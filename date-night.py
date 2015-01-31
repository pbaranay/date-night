# coding=utf-8

from flask import Flask
from flask import render_template
from flask import request
import dill
from flask_bootstrap import Bootstrap

app = Flask(__name__)

d = dill.load(open("static/d.dill"))
inv_d = dill.load(open("static/inv_d.dill"))
lookup_name = dill.load(open("static/lookup_name.dill"))
lookup_id = dill.load(open("static/lookup_id.dill"))
average_similarity = dill.load(open("static/average_similarity.dill"))
#svd = dill.load(open("static/svd.dill"))

@app.route('/')
def index():
    return render_template('bootstrap_test.html')

@app.route('/old')
def old_index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def index_post_form():
    a = request.form['yours']
    b = request.form['theirs']
    try:
        recos = average_similarity(a, b)
        recos = [x.title() for x in recos]
    except:
        recos = ["Error - Sorry! Please try again."]
        # TODO: add nicer error page
    return render_template('bootstrap_recommendations.html', yours=a, theirs=b, recos=recos[0:5])
#    return render_template('recommendations.html', a=a, b=b, recos=recos)

@app.route('/about')
def about():
    return render_template('bootstrap_about.html')

@app.route('/typeahead')
def typeahead():
    return render_template('the-basics.html')

if __name__ == '__main__':
    Bootstrap(app)
    app.run(host='0.0.0.0', debug=True)
