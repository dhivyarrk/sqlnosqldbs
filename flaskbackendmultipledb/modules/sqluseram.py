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

class SqlUserAMList(restful.Resource):
    
    def get(self):
        q = SqlUserAM.query.all()  
        #import jsonpickle
        #j = jsonpickle.encode(q)
        #return j
        #return render_template('users_am.html', q=q)
        
        # TODO: fix this properly
        html_content = render_template('users.html', q=q, database="Sql", table= "useram")
        return Response(html_content, mimetype='text/html')

    def post(self):
        #name = request.form.get('name')
        #age = request.form.get('age')
        # Use the RESTful API endpoint to add the user
        #response = PostgresUsersAPI().post()
        user_name = request.form.get('name')
        current_time = datetime.datetime.now()
        #try:
        user = SqlUserAM(user_name=user_name, join_date=current_time)
        db.session.add(user)
        db.session.commit()
        q = SqlUserAM.query.all()
        html_content = render_template('users.html', q=q, database="Sql", table= "useram", new_user=user_name)
        return Response(html_content, mimetype='text/html')


