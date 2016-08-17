from flask.ext.wtf import Form
from wtforms import StringField, FloatField
from wtforms.validators import DataRequired, Length
from wtforms.fields.html5 import DateField

from cafecofi.common import messages


class CoffeePromoForm(Form):
    coffee_shop_id = StringField(messages.coffee_promo_coffee_shop_id_field,
                                 [DataRequired(messages.coffee_promo_coffee_id_required),
                                  Length(max=5,
                                         message="Id incorrecto")], )

    name = StringField(messages.coffee_promo_name_field, [DataRequired(messages.coffee_promo_name_required),
                                                          Length(max=50,
                                                                 message=messages.coffee_promo_name_length_check)], )
    # filters=(strip_tags, strip_filter))
    description = StringField(messages.coffee_promo_description_field,
                              [DataRequired(messages.coffee_promo_description_required),
                               Length(max=128, message=messages.coffee_promo_description_length_check)], )

    expiration_date = DateField(messages.coffee_promo_expiration_date_field,
                                [DataRequired(messages.coffee_promo_expiration_date_required)], )

    price = FloatField(messages.coffee_promo_price_field, [DataRequired(messages.coffee_promo_price_required), ])
