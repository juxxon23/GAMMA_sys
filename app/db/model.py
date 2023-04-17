from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    
    __tablename__ = 'User'

    business_id = db.Column(db.Integer, primary_key=True, nullable=False,
                            index=True)
    business_name = db.Column(db.String(30), nullable=False)
    business_email = db.Column(db.String(60), nullable=False)
    business_password = db.Column(db.String(128), nullable=False)
    comercial_activity = db.Column(db.String(40), nullable=False)
    plan_type = db.Column(db.Integer, nullable=False)
    # Plan_type sera una llave foranea.

    def __init__(self, business_name, business_email, business_password,
                 comercial_activity, plan_type):
        self.business_name = business_name
        self.comercial_activity = comercial_activity
        self.plan_type = plan_type
        self.business_email = business_email
        self.business_password = business_password

class Product(db.Model):
    
    __tablename__ = 'Product'

    product_id = db.Column(db.String(10), primary_key=True, nullable=False)
    product_name = db.Column(db.String(30), nullable=False)
    product_description = db.Column(db.String(60), nullable=False)
    product_price = db.Column(db.Float, nullable=False)

    def __init__(self, product_id, product_name, product_description,
                 product_price):
        self.product_id = product_id
        self.product_name = product_name
        self.product_description = product_description
        self.product_price = product_price

