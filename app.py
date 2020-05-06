"""
@author: BO DINCER
@uni: bd2561
@page: https://freemantdsfdsf.pythonanywhere.com/
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    '''
    RENDERS TO THE HOME PAGE TEMPLATE
    '''
    return render_template('home.html')

@app.route('/about/')
def about():
    '''
    RENDERS TO THE ABOUT PAGE TEMPLATE
    '''
    return render_template('about.html')

@app.route('/assignments/')
def assignments():
    '''
    RENDERS TO THE ASSIGNMENTS PAGE TEMPLATE
    '''
    return render_template('assignments.html')

if __name__ == '__main__':
    app.run()
