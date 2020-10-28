from flask import render_template
from app import flask_app

@flask_app.route('/')
@flask_app.route('/index')
def index():
    user = {'username': 'User1'}
    posts = [
        {
            'author': {'username': 'User2'},
            'body': 'Wonderful day in Canada...'
        },
        {
            'author': {'username': 'User3'},
            'body': 'We the North'
        },
        {
            'author': {'username': 'User4'},
            'body': 'Eh!'
        },
        {
            'author': {'username': 'User5'},
            'body': 'Maple Leaf'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)