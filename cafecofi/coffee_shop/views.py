from flask import flash, render_template, redirect, url_for

from cafecofi import db, app
from cafecofi.coffee_shop.forms import CoffeeShopRegistrationForm
from cafecofi.common import messages
from .models import CoffeeShop


@app.route('/thanks')
def thanks():
    return render_template('./thanks.html')


@app.route('/coffee_shops', methods=['GET', 'POST'])
def add_coffee_shop():
    form = CoffeeShopRegistrationForm()
    if form.validate_on_submit():
        coffee_shop = CoffeeShop(name=form.name.data, manager_name=form.manager_name.data, email=form.email.data)
        db.session.add(coffee_shop)
        db.session.commit()
        flash(messages.coffee_shop_successfully_added.format(coffee_shop.name), 'success')
        return redirect(url_for('thanks'))
    return render_template('coffee_shop/registration.html', form=form)
