from cafecofi import db


class CoffeeShop(db.Model):
    __tablename__ = 'coffee_shops'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    email = db.Column(db.String(70), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    manager_name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return self.id + self.name
