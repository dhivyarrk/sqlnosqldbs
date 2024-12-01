from pymongo import MongoClient


#app.config.from_object(SqlnosqldbConfig)
    
mongo_client = MongoClient(app.config['MONGO_URI'])
mongo_db = mongo_client[app.config['MONGO_DB_NAME']]
