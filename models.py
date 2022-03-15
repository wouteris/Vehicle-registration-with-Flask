from __init__ import db
from sqlalchemy.sql import func
from flask import Blueprint

models = Blueprint('models', __name__)

class vehicle_group(db.Model):
    vehicle_groupid = db.Column(db.Integer, primary_key=True)
    vehicle_groupdescription = db.Column(db.String(10000))
    vehicle_groupstatus = db.Column(db.String(10000))

class vehicle(db.Model):
    vehicleid = db.Column(db.Integer, primary_key=True)
    vehicledescription = db.Column(db.String(10000))
    vehicle_group = db.Column(db.String(10000))
    vehiclestatus = db.Column(db.String(10000))
    

