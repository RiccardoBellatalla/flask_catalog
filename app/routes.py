from flask import render_template
from app import application
app = application

@app.route('/')
@app.route('/index')
def index():
    user = {'username' : 'Riccardo'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
