import os
from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def student():
    return render_template('index.html')

@app.route('/train')
def train():
    return render_template('train.html')

@app.route('/train', methods=['POST'])
def my_form_post():
    action = request.form['text']
    args="python -m pygarl record -p COM -d . -g "+action+" -a 11 -m discrete"
    print(args)
    os.system(str(args))
    return render_template('train.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        o_id = request.form['offense_id']
        oc_id = request.form['offense_category_id']
        lat = request.form['lon']
        lon = request.form['lat']

        if "1" in str(result):
            return ' is 1- crime '
        elif "0" in str(result):
            return ' is 0-not crime'


if __name__ == '__main__':
    app.run(debug=True)
