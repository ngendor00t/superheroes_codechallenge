from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Hero(db.Model):
    __tablename__ ='heroes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.integer)




class Power(db.Model):
    __tablename__='powers'


    id = db.Column(db.integer,primary_key = True)
    number_of_powers = db.column(db.string)

