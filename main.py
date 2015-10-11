# encoding: utf8


from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    print 'require index'
    return jsonify({
        'test': 'test'
    })


@app.route('/test')
def test():
    return 'Hello, Fucking bastard'


@app.route('/registration/<int:country>/<phone_number>', methods=['GET', 'POST'])
def registration(country, phone_number):
    print 'require regisration'
    some_error = False
    if some_error:
        return jsonify({
            'error': True,
            'reason': 'Something'
        })
    else:
        confirmation_code = 42
        return jsonify({
            'error': False,
            'number': phone_number,
            'country': country,
            'confirmation': confirmation_code
        })


if __name__ == '__main__':
    app.run(debug=True)
