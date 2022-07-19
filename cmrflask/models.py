from datetime import datetime
from cmrflask import db, login_manager
from flask_login import UserMixin 

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    CMRS = db.relationship('CMR', lazy=True)
    
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')" 
    
class CMR(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.Text, nullable=False)
    consignee = db.Column(db.Text, nullable=False)
    carrier = db.Column(db.Text, nullable=False)
    placeofdevliery = db.Column(db.Text, nullable=False)
    successivecarriersnames = db.Column(db.Text)
    placeoftakinggoods = db.Column(db.Text, nullable=False)
    dateoftakinggoods = db.Column(db.DateTime(), nullable=False)
    carrierreservs = db.Column(db.Text)
    annexeddocs = db.Column(db.Text)
    senderinstructions = db.Column(db.Text)
    directionsfreight = db.Column(db.Text)
    freightpaid = db.Column(db.Boolean)
    freightToBePaid = db.Column(db.Boolean)
    EstablishedIn = db.Column(db.String(60))
    EstablishedOn = db.Column(db.DateTime)
    specialagreements = db.Column(db.String(255))
    goods = db.relationship('Goods', lazy=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    form_data = db.Column(db.String)
    
    def __repr__(self):
        return f"CMR('{self.id}', '{self.sender}', '{self.carrier}')" 

class Goods(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    marksandnumbers = db.Column(db.String(30))
    numberOfPackages = db.Column(db.Integer)
    methodOfPacking = db.Column(db.String(50))
    natureOfGoods = db.Column(db.String(60))
    statisticalnumber = db.Column(db.Integer)
    grossweight = db.Column(db.Float)
    volume = db.Column(db.Float)
    Class = db.Column(db.String(10))
    Number = db.Column(db.Integer)
    Letter = db.Column(db.String(10))
    ADR = db.Column(db.String(10))
    cmr_id = db.Column(db.Integer, db.ForeignKey('CMR.id'), nullable=False)

