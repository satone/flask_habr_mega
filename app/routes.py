from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Raodiaon Hahapetoff'}
    posts = [
        {'author': {'username': 'John'},
         'body': 'Beautefault day in portland cement!'
         },
        {'author': {'username': 'Susan'},
         'body': 'Abengers are cool@'
         },
        {'author': {'username': 'Иппа'},
         'body': 'Какая гадость эта ваша заливная рыба"'
         }
    ]

    return render_template('index.html', title='Home', user=user, posts=posts)
