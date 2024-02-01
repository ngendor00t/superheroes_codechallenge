from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Hero(db.Model):
    __tablename__ ='heroes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    super_name = db.Column(db.Integer)
    created_at =db.Column(db.DateTime,server_default=db.func.now())
    updated_at =db.Column(db.DateTime,onupdate=db.func.now())

    

    hero_powers = db.relationship('HeroPower', backref ='hero')

    
    def __repr__(self): 
        return f'<hero {self.name} , {self.age}>'                  


class Power(db.Model):
    __tablename__='powers'


    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.Integer)
    description =db.Column(db.String)
    created_at =db.Column(db.DateTime,server_default=db.func.now())
    updated_at =db.Column(db.DateTime,onupdate=db.func.now())

    hero_powers =db.relationship('HeroPower', backref ='power')
                                            

    @validates("description")
    def validate_description(self,key,value):
        if not value or len (value) < 7:
            raise ValueError("failed power validation")
        return value 
        
    def __repr__(self) :
        return f' <Power {self.number_of_powers},{self.description}>'


class HeroPower(db.Model):
    __tablename__='heropowers'

    
    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String)
    created_at =db.Column(db.DateTime,server_default=db.func.now())
    updated_at =db.Column(db.DateTime,onupdate=db.func.now())

    hero_id = db.Column(db.Integer ,db.ForeignKey('heroes.id'))
    power_id =db.Column(db.Integer, db.ForeignKey('powers.id'))

                                       
    
    @validates('strength')
    def validate_strength(self,key,value):
        if not value or len(value)< 4:
            raise ValueError("failed heropower validation")
        return value 
    

    def __repr__(self):
        return f'<heropower{self.strength}'
        




    