from flaskbackendmultipledb.database import db

class SqlUserAM(db.Model):
    __tablename__ = 'users_am'

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(), nullable=False)
    join_date = db.Column(db.DateTime, nullable=False)

class SqlUserNZ(db.Model):
    __tablename__ = 'users_nz'

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(), nullable=False)
    join_date = db.Column(db.Date, nullable=False)


class SqlGenericProducts(db.Model):
    __tablename__ = 'generic_products'

    product_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_name = db.Column(db.String(), nullable=False)
    product_description = db.Column(db.String(), nullable=False)


class SqlRegionalProducts(db.Model):
    __tablename__ = 'regional_products'

    product_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_name = db.Column(db.String(), nullable=False)
    product_description = db.Column(db.String(), nullable=False)
    

class SqlUserAMmembership(db.Model):
    __tablename__ = 'users_am_membership'

    user_id = db.Column(db.Integer, db.ForeignKey('users_am.user_id'), primary_key=True, nullable=False)
    membership = db.Column(db.String(), nullable=False, default='regular')
    
    __table_args__ = (
        db.CheckConstraint(membership.in_(['regular', 'premium']), name='member_types'),
    )
   

class SqlUserNZmembership(db.Model):
    __tablename__ = 'users_nz_membership'

    user_id = db.Column(db.Integer, db.ForeignKey('users_nz.user_id'), primary_key=True, nullable=False)
    membership = db.Column(db.String(), nullable=False, default='regular')
    
    __table_args__ = (
        db.CheckConstraint(membership.in_(['regular', 'premium']), name='member_types'),
    )


class SqlMetadata(db.Model):
    __tablename__ = 'metadata_europe'

    metadata_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    metadata_info = db.Column(db.String(), nullable=False)