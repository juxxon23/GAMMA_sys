from flask.views import MethodView
from flask import request, jsonify

from app.db.model import Product
from app.db.dbtool import DBTool

import random

dbt = DBTool()

class Products(MethodView):

    def get(self):
        try:
            prod_sto = dbt.get_all(Product) # products stored
            prod_list = []
            for prod in prod_sto:
                p = {
                        'productId': prod.product_id,
                        'productName': prod.product_name,
                        'productDescription': prod.product_description,
                        'productPrice': prod.product_price,
                        }
                prod_list.append(p)
            return jsonify({'status': 'GET Products', 'products': prod_list})
        except Exception as ex:
            return jsonify({'status': 'exception', 'ex': str(ex)})

    def post(self):
        try:
            prod_log = request.get_json()
            new_prod = Product(
                    product_id = random.randint(0, 1978),
                    product_name = prod_log['productName'],
                    product_description = prod_log['productDescription'],
                    product_price = float(prod_log['productPrice']))
            state = dbt.add(new_prod)
            return jsonify({'status': state})
        except Exception as ex:
            return jsonify({'status': 'exception', 'ex': str(ex)})
