from app import db

class Result(db.Model):
    __tablename__ = 'results'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String())
    result_all = db.Column(db.Text())
    result_no_stop_words = db.Column(db.Text())

    def __init__(self, url, result_all, result_no_stop_words):
        self.url = url
        self.result_all = result_all
        self.result_no_stop_words = result_no_stop_words

    def __repr__(self):
        return '<id {}>'.format(self.id)

class User(db.Model):
    __tablename__ = "users"

    id_user = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(60))
    mail = db.Column(db.String(60))
    first_name = db.Column(db.String(60))
    last_name = db.Column(db.String(60))
    password = db.Column(db.String(60))
    addresses = db.relationship('Address', backref='user',
                                lazy='dynamic')
    
    def __init__(self,initial_data = None):
        if initial_data is None:
            return
        for key in initial_data:
            try:
                setattr(self, key, initial_data[key])    
            except AttributeError as e:
                print(e)
            except ValueError as e:
                print(e)
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.Text())
    users_id_user = db.Column(db.Integer, db.ForeignKey('users.id_user'))
    