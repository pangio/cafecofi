from flask.ext.wtf import Form
from wtforms import StringField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length

from cafecofi.common import messages


class CoffeeShopRegistrationForm(Form):
    name = StringField(messages.coffee_shop_name_field, [DataRequired(messages.coffee_shop_name_required),
                                                         Length(max=50,
                                                                message=messages.coffee_shop_name_max_length_check)], )
    # filters=(strip_tags, strip_filter))
    manager_name = StringField(messages.coffee_shop_manager_name_field,
                               [DataRequired(messages.coffee_shop_manager_name_required),
                                Length(max=70, message=messages.coffee_shop_manager_name_max_length_check)], )

    email = EmailField(messages.coffee_shop_email_field, [DataRequired(messages.coffee_shop_email_required),
                                             Length(max=50, message=messages.coffee_shop_manager_name_required)],)
