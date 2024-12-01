from flask import g, current_app, Response, request    
from flask import Flask, render_template
from flaskbackendmultipledb.database import db
from flaskbackendmultipledb.models.sqlmodels import SqlUserAM, SqlRegionalProducts #, EuropeUserNZ, EuropeGenericProducts, EuropeUserAMmembership, EuropeUserNZmembership, EuropeMetadata_Europe
import flask_restful as restful
from flask import jsonify
import json
import datetime

#blueprint = Blueprint('db1', __name__, url_prefix='/db1')
#blueprint = Blueprint('carsdb2',__name__)

class SqlNosqlRegionalProducts(restful.Resource):
    
    def get(self):
        # Query PostgreSQL products
        sql_regionalproducts = SqlRegionalProducts.query.all()
        products_map = {
            product.product_id: {"product_name": product.product_name, "product_description": product.product_description}
            for product in sql_regionalproducts
        }
        # Query MongoDB products
        mongo_db = current_app.mongo_db
        nosql_regionalproducts = list(mongo_db.products.find())  
        
        # Combine data
        combined = []
        for product in nosql_regionalproducts:
            product_data = products_map.get(int(product['_id']), {"product_name": "product_name", "product_description": "product_description"})
            combined.append({
                "_id": product['_id'],
                "postgres_product_name": product_data['product_name'],
                "postgres_product_description": product_data['product_description'],
                "mongodb_product_name": product['product_name'],
                "mongodb_product_description": product['product_description']
            })
        
        html_content = render_template('sqlnosql.html', products=combined, database="SqlNosql")
        return Response(html_content, mimetype='text/html')

"""
# reverse join

class SqlNosqlRegionalProducts(restful.Resource):
    
    def get(self):
        # Query PostgreSQL products
        sql_regionalproducts = SqlRegionalProducts.query.all()
        nosql_regionalproducts = list(mongo_db.products.find()) 
        product_ids = {product['_id'] for product in nosql_regionalproducts}  

        products_map = {
            product.product_id: {"product_name": product.product_name, "product_description": product.product_description}
            for product in sql_regionalproducts
        }
        print("PostgreSQL Users:", products_map)
        # Query MongoDB products
        mongo_db = current_app.mongo_db
        nosql_regionalproducts = list(mongo_db.products.find())  
        print("nosql_regionalproducts", nosql_regionalproducts)

        # Combine data
        combined = []
        for product in nosql_regionalproducts:
            product_data = products_map.get(int(product['_id']), {"product_name": "product_name", "product_description": "product_description"})
            combined.append({
                "_id": product['_id'],
                "product_name": product_data['product_name'],
                "product_description": product_data['product_description']
            })
        print("product_data:", product_data)
        print("Combined", combined)

        html_content = render_template('sqlnosql.html', products=combined, database="SqlNosql")
        return Response(html_content, mimetype='text/html')
"""