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

class SqlRegionalProductsList(restful.Resource):
    
    def get(self):
        q = SqlRegionalProducts.query.all()  
        html_content = render_template('products.html', q=q, database="Sql", table= "regionalproducts")
        return Response(html_content, mimetype='text/html')
    
    def post(self):
        """Handle form actions for PostgreSQL Users."""
        action = request.form.get('action')
        if action == 'add':
            product_name = request.form.get('product_name')
            product_description = request.form.get('product_description')
            product = SqlRegionalProducts(product_name=product_name, product_description=product_description)
            db.session.add(product)
            db.session.commit()
            q = SqlRegionalProducts.query.all()
            html_content = render_template('products.html', q=q, database="Sql", table= "regionalproducts", new_product=product_name)
            return Response(html_content, mimetype='text/html')

        if action == 'delete':
            product_name = request.form.get('product_name')
            product = SqlRegionalProducts.query.filter_by(product_name=product_name).first()
            db.session.delete(product)
            db.session.commit()
            q = SqlRegionalProducts.query.all()
            html_content = render_template('products.html', q=q, database="Sql", table= "regionalproducts", deleted_product=product_name)
            return Response(html_content, mimetype='text/html')

        if action == 'modify':
            'Modify a user in PostgreSQL.'
            product_name = request.form.get('product_name')
            product_description = request.form.get('product_description')
            product = SqlRegionalProducts.query.filter_by(product_name=product_name).first()
            if not product:
                return {'error': 'User not found'}, 404
            product.product_description = product_description
            db.session.commit()
            q = SqlRegionalProducts.query.all()
            html_content = render_template('products.html', q=q, database='Sql', table= 'regionalproducts', modified_product=product_name)
            return Response(html_content, mimetype='text/html')

