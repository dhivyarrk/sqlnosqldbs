import datetime
import flask_restful as restful
from pymongo import MongoClient
from flask import current_app, render_template, Response, request, redirect, url_for

#from flaskbackendmultipledb import app

#from flaskbackendmultipledb import app
#app.config.from_object(SqlnosqldbConfig)
    
#mongo_client = MongoClient(app.config['MONGO_URI'])
#mongo_db = mongo_client[app.config['MONGO_DB_NAME']]
#mongo_db = current_app.mongo_db
#from flaskbackendmultipledb.nosqldatabase import mango_db

class NosqlMongoRegionalProducts(restful.Resource):
    def get(self):
        """Render MongoDB Products Page."""
        mongo_db = current_app.mongo_db
        products = mongo_db.products.find()
        html_content = render_template("mongoproducts.html", products=products, database="NoSql")
        return Response(html_content, mimetype='text/html')
        
    def post(self):
        mongo_db = current_app.mongo_db

        """Handle form actions for MongoDB Users."""
        action = request.form.get('action')
        print(action)
        if action == 'add':
            # Add a new user
            product_id = request.form.get('product_id')
            product_name = request.form.get('product_name')
            product_description = request.form.get('product_description')
            try:
                mongo_db.products.insert_one({"_id": product_id, "product_name": product_name, "product_description": product_description})
                products = mongo_db.products.find()
                html_content = render_template("mongoproducts.html", products=products, database="NoSql", new_product=product_name)
                return Response(html_content, mimetype='text/html')
            except Exception as e:
                return {"error": str(e)}, 500

        elif action == 'modify':
            # Modify an existing user
            print("modify")
            product_name = request.form.get('product_name')
            product_description = request.form.get('product_description')
            print(product_name)
            print(product_name)
            filter_query = {'product_name': product_name}
            print("in here")
            update_query = {'$set': {'product_description': product_description}}
            print("y")
            result = mongo_db.products.update_one(filter_query, update_query)
            print("w")
            if result.matched_count == 0:
                return {"error": "Product not found"}, 404
            products = mongo_db.products.find()
            html_content = render_template("mongoproducts.html", products=products, database="NoSql", modified_product=product_name)
            return Response(html_content, mimetype='text/html')
        

        elif action == 'delete':
            # Delete a user
            product_name = request.form.get('product_name')
            result = mongo_db.products.delete_one({'product_name': product_name})
            if result.deleted_count == 0:
                return {"error": "Product not found"}, 404
            products = mongo_db.products.find()
            html_content = render_template("mongoproducts.html", products=products, database="NoSql", deleted_product=product_name)
            return Response(html_content, mimetype='text/html')