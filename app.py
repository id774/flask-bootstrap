# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect, url_for
from flask.ext.assets import Environment
from hamlish_jinja import HamlishTagExtension
import numpy as np

app = Flask(__name__)

# Haml Extension
app.jinja_env.add_extension(HamlishTagExtension)

# Compile assets
assets = Environment(app)
assets.url = app.static_url_path

# Main
def picked_up():
    messages = [
        "こんにちは、あなたの名前を入力してください",
        "やあ！お名前は何ですか？",
        "あなたの名前を教えてね"
    ]
    return np.random.choice(messages)

# Routing
@app.route('/')
def index():
    message = picked_up()
    return render_template('index.html', message=message)

@app.route('/post', methods=['POST', 'GET'])
def post():
    if request.method == 'POST':
        name = request.form['name']
        return render_template('index.html', name=name)
    else:
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0')
