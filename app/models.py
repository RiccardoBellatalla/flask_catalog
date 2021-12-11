from datetime import datetime
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    company_name = db.Column(db.String(100), index=True, unique=False)
    products = db.relationship('Product', backref='seller_owner', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sku_seller = db.Column(db.String(64), index=True, unique=True)
    ean_code = db.Column(db.String(16), index=True, unique=False)
    brand = db.Column(db.String(64), index=True, unique=False)
    product_title = db.Column(db.String(128), index=False, unique=False)
    product_description = db.Column(db.String(2048), index=False, unique=False)
    product_price = db.Column(db.Numeric(10,2), unique=False)
    stock = db.Column(db.Integer, unique=False)
    img_1 = db.Column(db.String(500), index=False, unique=True)
    carrier = db.Column(db.String(64), index=False, unique=False)
    shipping_price = db.Column(db.Numeric(10,2), unique=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Product {}>'.format(self.sku_seller)

#    body = db.Column(db.String(140))
#    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
#    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

#    def __repr__(self):
#        return '<Post {}>'.format(self.body)
