from datetime import datetime
from flask import flash
from cafecofi import db
from cafecofi.coffee_promos.forms import CoffeePromoForm
from cafecofi.coffee_promos.models import CoffeePromo
from flask import flash, render_template, redirect, url_for

from cafecofi import db, app
from cafecofi.common import messages

@app.route('/thanks_promo')
def thanks_promo():
    return render_template('./thanks.html')


@app.route('/coffee_promo', methods=['GET', 'POST'])
def add_coffee_promo():
    form = CoffeePromoForm()
    if form.validate_on_submit():
        coffee_promo = CoffeePromo()
            # (name=form.name.data, description='desc', expiration_date=datetime.utcnow(),
            #                    coffee_shop_id=12, price=12000)
        form.populate_obj(coffee_promo)
        db.session.add(coffee_promo)
        db.session.commit()
        flash(messages.coffee_promo_successfully_added.format(coffee_promo.name, coffee_promo.coffee_shop_id), 'success')
        return redirect(url_for('thanks'))
    return render_template('coffee_promo/new_promo.html', form=form)
