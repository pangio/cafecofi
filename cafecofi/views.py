from flask import render_template
from cafecofi import app

# TODO import all views here
from coffee_shop import views
from coffee_promo import views
from clients import views

@app.route('/')
def home():
    return render_template('home.html')

# @app.route('/thanks')
# def thanks():
#     return render_template('templates/thanks.html')

