from cafecofi import db
from cafecofi.common import DEFAULT_WITH_DELETE_CASCADE


class CoffeePromo(db.Model):
    __tablename__ = 'coffee_promos'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(128), nullable=False)
    expiration_date = db.Column(db.DateTime(), nullable=False)
    coffee_shop_id = db.Column(db.Integer, db.ForeignKey('coffee_shops.id'), nullable=False, index=True)
    price = db.Column(db.NUMERIC, nullable=False)

    coffee_shop = db.relationship('CoffeeShop',
                                  backref=db.backref('promos',
                                                     lazy='dynamic',
                                                     cascade=DEFAULT_WITH_DELETE_CASCADE))
