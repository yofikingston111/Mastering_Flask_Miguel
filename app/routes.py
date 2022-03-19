from flask import render_template
from app import app
from app.forms import LoginForm
# from flask import render_template, flash, redirect

#Home page route

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign in', form=form)

    # posts = [
    #     {
    #         'author':{'username': 'Rijaluddin'},
    #         'body':'The Body is sixpect!'
    #     },
    #     {
    #         'author': {'username': 'fery'},
    #         'body': 'The body is thin'
    #     }
    # ]



# <html>
#     <head>
#         <title>Home Page -Microblog</title>
#     </head>
#     <body>
#         <h1>Hello, ''' + user['username']+'''!</h1>
#     </body>
# </html>'''
#
    


