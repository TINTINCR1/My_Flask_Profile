# In Flask, views are typically defined in app.py or blueprints.
# For clarity, here's how you can separate the view:

from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html', name="Luis")
