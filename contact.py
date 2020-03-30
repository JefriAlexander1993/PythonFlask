from app import db


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(50))
    email = db.Column(db.String(50))
    phone = db.Column(db.String(50))


    def __init__(self, fullname=None,email=None,phone=None):
            self.fullname= fullname
            self.email= email
            self.phone=phone