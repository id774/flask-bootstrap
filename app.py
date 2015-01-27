from flask import Flask, render_template
from flask.ext.assets import Environment, Bundle
from hamlish_jinja import HamlishTagExtension
from flask import request
import numpy as np

app = Flask(__name__)
app.debug = True

# Haml Extension
app.jinja_env.add_extension(HamlishTagExtension)

# Compile assets
assets = Environment(app)
assets.url = app.static_url_path

# Stylesheets
css_bundle = Bundle(
    'css/common.css.sass', filters='sass', output='common.css')
assets.register('css_common', css_bundle)
css_bundle = Bundle(
    'css/bootstrap.css', filters='sass', output='bootstrap.css')
assets.register('css_bootstrap', css_bundle)

# JavaScript
js_bundle = Bundle(
    'js/common.js.coffee', filters='coffeescript', output='common.js')
assets.register('js_common', js_bundle)

# Code
def picked_up():
    names = ["山田", "田中", "鈴木"]
    return np.random.choice(names)

# Routing
@app.route('/post', methods=['POST', 'GET'])
def post():
    if request.method == 'POST':
        return render_template('index.html.haml')
    else:
        name = picked_up()
        return render_template('result.html.haml', name=name)

@app.route('/')
def hello_word():
    return render_template('index.html.haml')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
