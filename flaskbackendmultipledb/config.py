class SqlnosqldbConfig(object):
    SQLALCHEMY_DATABASE_URI = "postgresql://db_user:12345@127.0.0.1:5432/sql_database"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MONGO_URI = "mongodb://localhost:27017"
    MONGO_DB_NAME = "nosql_database"
    