# encoding: utf8


from flask import Flask, jsonify
from flask_mail import Message, Mail

app = Flask(__name__)
mail = Mail(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    print 'require index'
    return jsonify({
        'test': 'test'
    })


class User:
    def __init__(self, phone_number):
        self.__pnone_number = phone_number
        self.__name = ''
        self.__last_name = ''

    def setName(self, name):
        self.__name = name

    def setLastName(self, lastName):
        self.__last_name = lastName

    def __eq__(self, other):
        return self.__pnone_number == other.__phone_number and self.__name == other.__name and self.__last_name == other.__last_name

    def generateConfirm(self):
        return 42


class Users:
    def __init__(self):
        self.__users = []

    def addUser(self, user):
        f = filter(lambda u: u == user, self.__users)
        if not f:
            self.__users.append(user)

    def confirmCode(self, phone, confirm):
        pass


@app.route('/registration/<int:country>/<phone_number>', methods=['GET', 'POST'])
def registration(country, phone_number):
    some_error = False
    if some_error:
        return jsonify({
            'error': True,
            'reason': 'Something'
        })
    else:
        confirmation_code = 42
        with mail.connect() as conn:
            msg = Message(subject='Confirm Code', recipients=[str(phone_number)],
                          body='Your confirmaion code is: {}'.format(confirmation_code),
                          sender='shnaiderpasha@gmail.com')
            msg.send(conn)
        return jsonify({
            'error': False,
            'number': str(phone_number),
            'country': str(country),
            'confirmation': str(confirmation_code)
        })


@app.route('/confirmation/<phone_number>/<confirmation_code>', methods=['GET', 'POST'])
def confirmation(phone_number, confirmation_code):
    some_error = False
    if some_error:
        return jsonify({
            'error': True,
            'reason': 'invalid confirmation code'
        })
    else:
        confirmation_code = 42
        return jsonify({
            'error': False,
            'number': str(phone_number),
            'confirmed': True
        })


@app.route('/confirmation/<phone_number>/<name>/<last_name>', methods=['GET', 'POST'])
def confirmation(phone_number, name, last_name):
    some_error = False
    if some_error:
        return jsonify({
            'error': True,
            'reason': 'can\' register name and last name'
        })
    else:
        return jsonify({
            'error': False,
            'number': str(phone_number),
            'name': name,
            'last_name': last_name,
            'registered': True
        })


if __name__ == '__main__':
    app.run(debug=True)
