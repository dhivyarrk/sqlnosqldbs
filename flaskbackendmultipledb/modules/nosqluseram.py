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

class NosqlMongoUsers(restful.Resource):
    def get(self):
        """Render MongoDB Users Page."""
        mongo_db = current_app.mongo_db
        users = mongo_db.users.find()
        html_content = render_template("mongousers.html", users=users, database="NoSql", table= "useram")
        return Response(html_content, mimetype='text/html')
        
    def post(self):
        mongo_db = current_app.mongo_db

        """Handle form actions for MongoDB Users."""
        action = request.form.get('action')
        print(action)
        if action == 'add':
            # Add a new user
            user_name = request.form.get('user_name')
            user_id = request.form.get('user_id')

            current_time = datetime.datetime.now()
            try:
                mongo_db.users.insert_one({"_id": user_id, "user_name": user_name, "join_date": current_time})
                users = mongo_db.users.find()
                html_content = render_template("mongousers.html", users=users, database="NoSql", table= "useram", new_user=user_name)
                return Response(html_content, mimetype='text/html')
            except Exception as e:
                return {"error": str(e)}, 500

        elif action == 'modify':
            # Modify an existing user
            name = request.form.get('name')
            age = request.form.get('age')
            filter_query = {'name': name}
            update_query = {'$set': {'age': int(age)}}
            result = mongo_db.users.update_one(filter_query, update_query)
            if result.matched_count == 0:
                return {"error": "User not found"}, 404

        elif action == 'delete':
            # Delete a user
            name = request.form.get('name')
            result = mongo_db.users.delete_one({'name': name})
            if result.deleted_count == 0:
                return {"error": "User not found"}, 404

        #return redirect(url_for('mongopage'))