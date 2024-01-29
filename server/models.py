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
    number_of_powers = db.Column(db.Integer)
    description =db.Column(db.String)


    Hero= db.relationship('hero', backref ='Power')

    @validates("description")
    def validate_description(self,key,description):
        if "length" not in description :
            raise ValueError("failed power validation")
        
    def __repr__(self) :
        return f' <Power {self.number_of_powers},{self.description}>'


class HeroPower(db.Model):
    __tablename__='heropowers'

    
    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String)

    # hero_id = db.Column (db.Integer ,db.Foreignkey('heroes.id'))
    # power_id =db.Column (db.Integer, db.Foreignkey('powers.id'))

    hero = db.relationship('Hero', backref ='heropower')
    power =db.relationship('Power', backref ='heropower')
                                               
    
    @validates('strength')
    def validate_strength(self,key,strength):
        if "presence" not in strength:
            raise ValueError("failed heropower validation")
    

    def __repr__(self):
        return f'<heropower{self.strength}'
        




    