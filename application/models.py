from sqlalchemy.orm import backref
from application import db

# Define the Hosts table in the DB
class Hosts(db.Model):
    host_id = db.Column(db.Integer, nullable=False, primary_key=True)
    host_name = db.Column(db.String(255), nullable=False)
    host_ip = db.Column(db.String(50), nullable=False)
    rules = db.relationship('Rules', backref='host')

# Define the Rules table in the DB
class Rules(db.Model):
    rule_id = db.Column(db.Integer, nullable=False, primary_key=True)
    port = db.Column(db.Integer, nullable=False)
    allow = db.Column(db.Boolean, nullable=False)
    host_id = db.Column('host_id',db.Integer, db.ForeignKey('hosts.host_id'), nullable=False)
