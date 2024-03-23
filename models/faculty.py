from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from extensions import db
from sqlalchemy import *
#test
#    "Faculty": {
#       "Name": "String",
#       "Department": "String",
#       "Positions": [{"PositionName": "String"}],
#       "Office Location": "String",
#       "Phone #": "String",
#       "Email": "String"

class Faculty(db.Model):
    __tablename__ = 'faculty'

    name = db.Column(db.String(255), nullable = False, primary_key = True)
    department = db.Column(db.String(255), nullable = False, primary_key = True)
    positions = db.Column(db.ARRAY(String(255)), nullable = False)
    officeLocation = db.Column(db.String(255), nullable = False)
    phoneNumber = db.Column(db.String(255), nullable = False)
    emailAddress = db.Column(db.String(255), nullable = False)

    def __repr__(self):
        return '<Faculty %r>' % self.name