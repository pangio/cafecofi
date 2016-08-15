from flask import render_template
from cafecofi import app


@app.route('/clients', methods=['GET', 'POST'])
def add_client():
    return render_template('clients/home.html')

@app.route('/clients/<int:id>/kit', methods=['GET', 'POST'])
def add_kit(id=None):
    return render_template('coming_soon.html')

