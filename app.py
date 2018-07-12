# /usr/bin/python3
# coding=utf-8

from flask import Flask, render_template
from app2 import page3, page4

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/page1')
def page1():
    return render_template('page1.html')


@app.route('/page2/<string:par>/')
def page2(par):
    if par == '2':
        return render_template('page22.html', name=par)
    else:
        return render_template('page21.html', name=par)


app.add_url_rule('/page3', view_func=page3)

app.add_url_rule('/page4/<string:par>', view_func=page4)


if __name__ == '__main__':
    app.run(port=5000)
