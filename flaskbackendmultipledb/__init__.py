from flask import Flask, render_template
from flask_migrate import Migrate
from flask_restful import Resource, Api
from flask_cors import CORS
from pymongo import MongoClient

from flaskbackendmultipledb.config import SqlnosqldbConfig
from flaskbackendmultipledb.database import db
from flaskbackendmultipledb.models.sqlmodels import SqlUserAM, SqlRegionalProducts
#, SqlUserNZ, SqlGenericProducts, SqlRegionalProducts, SqlUserAMmembership, SqlUserNZmembership, SqlMetadata
from flaskbackendmultipledb.modules.sqluseram import SqlUserAMList
from flaskbackendmultipledb.modules.sqlregionalproducts import SqlRegionalProductsList
#, AmericaUserNZList, AmericaGenericProductsList, AmericaRegionalProductsList, AmericaUserAMmembershipList, AmericaUserNZmembershipList, AmericaMetadata_AmericaList
from flaskbackendmultipledb.modules.nosqluseram import NosqlMongoUsers
from flaskbackendmultipledb.modules.nosqlregionalproducts import NosqlMongoRegionalProducts
from flaskbackendmultipledb.modules.sqlnosql import SqlNosqlRegionalProducts

def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY = "Miy_Secret_Key"
    )
    app.config.from_object(SqlnosqldbConfig)
    CORS(app, origins=['http://localhost:3000'])
    db.init_app(app)
    migrate = Migrate(app, db)
    api=Api(app)
    # MongoDB setup using PyMongo
    
    mongo_client = MongoClient(app.config['MONGO_URI'])
    #mongo_db = mongo_client[app.config['MONGO_DB_NAME']]
    #app.mongo_db = mongo_client.get_database()
    app.mongo_db = mongo_client[app.config['MONGO_DB_NAME']]

    api.add_resource(SqlUserAMList, '/sql/usersam')
    api.add_resource(SqlRegionalProductsList, '/sql/regionalproducts')
    #api.add_resource(NosqlMongoProducts, '/nosql/reigonalproducts', endpoint='mongopage')
    api.add_resource(NosqlMongoUsers, '/nosql/usersam')
    api.add_resource(NosqlMongoRegionalProducts, '/nosql/regionalproducts')
    api.add_resource(SqlNosqlRegionalProducts, '/sqlnosql/combinedregionalproducts')

    """
    api.add_resource(AmericaUserAMList, '/america/usersam')
    api.add_resource(AmericaUserNZList, '/america/usersnz')
    api.add_resource(AmericaGenericProductsList, '/america/genericproducts')
    api.add_resource(AmericaRegionalProductsList, '/america/regionalproducts')
    api.add_resource(AmericaUserAMmembershipList, '/america/userammembership')
    api.add_resource(AmericaUserNZmembershipList, '/america/usernzmembership')
    api.add_resource(AmericaMetadata_AmericaList, '/america/metadata')
    api.add_resource(EuropeUserAMList, '/europe/usersam')
    api.add_resource(EuropeUserNZList, '/europe/usersnz')
    api.add_resource(EuropeGenericProductsList, '/europe/genericproducts')
    api.add_resource(EuropeRegionalProductsList, '/europe/regionalproducts')
    api.add_resource(EuropeUserAMmembershipList, '/europe/userammembership')
    api.add_resource(EuropeUserNZmembershipList, '/europe/usernzmembership')
    api.add_resource(EuropeMetadata_EuropeList, '/europe/metadata')
    api.add_resource(AsiaUserAMList, '/asia/usersam')
    api.add_resource(AsiaUserNZList, '/asia/usersnz')
    api.add_resource(AsiaGenericProductsList, '/asia/genericproducts')
    api.add_resource(AsiaRegionalProductsList, '/asia/regionalproducts')
    api.add_resource(AsiaUserAMmembershipList, '/asia/userammembership')
    api.add_resource(AsiaUserNZmembershipList, '/asia/usernzmembership')
    """
    @app.route('/')
    def home():
        #return 'this is login'
        return render_template("basic.html")

    return app