# coding=utf-8

from flask import Flask
from flask import render_template
from flask import request
import dill
from flask_bootstrap import Bootstrap
import os
import sys

app = Flask(__name__)

#d = dill.load(open("static/d.dill"))
#inv_d = dill.load(open("static/inv_d.dill"))
#lookup_name = dill.load(open("static/lookup_name.dill"))
#lookup_id = dill.load(open("static/lookup_id.dill"))
#average_similarity = dill.load(open("static/average_similarity.dill"))
#svd = dill.load(open("static/svd.dill"))

@app.route('/')
def index():
    return render_template('bootstrap_test.html')

@app.route('/old')
def old_index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def index_post_form():
    print "foobar"
    try:
        print request.form
        print request.form.keys()
        a = request.form['yours']
        b = request.form['theirs']
        print "a: {0}, b: {1}".format(a,b)
    except Exception as e:
        print "exception!"
        print >> sys.stderr, e
    d = dill.load(open("static/d.dill"))
    inv_d = dill.load(open("static/inv_d.dill"))
    try:
        id_a = inv_d[a.lower()]  # lookup_id
        id_b = inv_d[b.lower()]  # lookup_id
    except Exception as e:
#        print >> sys.stderr, e
        recos = ["Error - Sorry! Please try again. (Error finding movie ID's.)"]
        # first argument has to be lower than second argument
    try:
        if id_a < id_b:
            recs_filepath = "static/recommendations/"+str(id_a)+"/"+str(id_b)
#            recs_filepath = os.path.join("static","recommendations",str(id_a), str(id_b))
            recos = dill.load(open(recs_filepath))
#            recos = dill.load(open("static/recommendations/"+str(id_a)+"/"+str(id_b)))
        elif id_a > id_b:
            recs_filepath = "static/recommendations/"+str(id_b)+"/"+str(id_a)
            recos = dill.load(open(recs_filepath))
#            recos = dill.load(open("static/recommendations/"+str(id_b)+"/"+str(id_a)))
        elif id_a == id_b:
            recos = ["Error - Please give me two different movies!"]
        recos = [x.title() for x in recos]
        # TODO: make the title'ing better (handle "of", "the", "Bug'S")
    except Exception as e:
#        print >> sys.stderr, e
        recos = ["Error - Sorry! Please try again. (Error finding recommendations.)"]
        # TODO: add nicer error page
    return render_template('bootstrap_recommendations.html', yours=a, theirs=b, recos=recos[0:5])
#    return render_template('recommendations.html', a=a, b=b, recos=recos)

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
