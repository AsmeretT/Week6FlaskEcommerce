# aka 'Controller' - the 'traffic controller' of the entire project. 
# the controller directly communicates with the view(HTML - to update as needed)
# and the model(model.py - to add/manipulate date)

from app import app
from flask import render_template, redirect, url_for

@app.route('/')
def home():
    return redirect(url_for('ig.posts'))
    
    return render_template('index.html')

@app.route('/about')
def someFunc():
    return render_template('about.html')

@app.route('/signup')
def signMeUp():
    return {'hi' : 'There'}