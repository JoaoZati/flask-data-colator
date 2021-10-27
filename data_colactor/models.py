from data_colactor import db


class Data(db.Model):
    __tablename__ = 'data'
    id = db.Column(db.Integer, primary_key=True)
    email_db = db.Column(db.String(150), unique=True)
    height_db = db.Column(db.Integer)

    def __init__(self, email_db, height_db):
        self.email_db = email_db
        self.height_db = height_db
