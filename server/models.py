from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Hero(db.Model):
    __tablename__ ='heroes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)



    Power_id = db.Column(db.Integer(), db.ForeignKey('powers.id'))
                         
    def __repr__(self): 
        return f'<hero {self.name} , {self.age}>'                  


class Power(db.Model):
    __tablename__='powers'


    id = db.Column(db.Integer,primary_key = True)
    number_of_powers = db.column(db.Integer)

    HeroPowers = db.relationship('heropowers', backref ='Power')

    @validates("description")
    def validate_description(self,key,description):
        if "length" not in description :
            raise ValueError("failed power validation")


class HeroPower(db.Model):
    __tablename__='heropowers'
    

    id = db.Column(db.Integer, primary_key=True)

    
    @validates('strength')
    def validate_strength(self,key,strength):
        if "presence" not in strength:
            raise ValueError("failed heropower validation")