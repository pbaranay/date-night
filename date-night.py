from flask import Flask
from flask import render_template
from flask import request
import dill

app = Flask(__name__)

d = dill.load(open("static/d.dill"))
inv_d = dill.load(open("static/inv_d.dill"))
lookup_name = dill.load(open("static/lookup_name.dill"))
lookup_id = dill.load(open("static/lookup_id.dill"))
average_similarity = dill.load(open("static/average_similarity.dill"))
svd = dill.load(open("static/svd.dill"))


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def index_post_form():
    a = request.form['movie-a']
    b = request.form['movie-b']
    recos = average_similarity(a, b)
    return render_template('recommendations.html', a=a, b=b, recos=recos)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
