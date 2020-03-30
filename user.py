import datetime
import bcrypt
from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50),unique=True,nullable=False)
    email = db.Column(db.String(50),unique=True)
    password = db.Column(db.String(50),nullable=False)
    file=db.Column(db.String(128),nullable=True)
    create_on = db.Column(db.DateTime, nullable=False)
    update_on = db.Column(db.DateTime, nullable=False)
    delete_on = db.Column(db.DateTime, nullable=True)
    
    def __init__(self, name=None,email=None, password=None,file=None, create_on=None, update_on=None,delete_on=None):
            self.name = name
            self.email = email
            self.password = password
            self.file = file
            self.create_on = datetime.datetime.now()
            self.update_on = datetime.datetime.now()
            self.delete_on = delete_on
      