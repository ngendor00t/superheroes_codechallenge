from flask import Flask
from flask import Flask, jsonify, request , make_response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from models import db,Hero,Power,HeroPower

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

Migrate = Migrate(app,db)

db.init_app(app)

@app.route('/heroes')
def heroes():
    heroes = []

    for hero in Hero.query.all():
        hero_dict ={
            "name" : hero.name,
            "age"  : hero.age
        
        }
        heroes.append(hero_dict)

        response = make_response(
        jsonify(heroes),
            200
        )
        return response  

    if __name__ == '__main__':
        app.run(port=5555)
                          
@app.route('/heroes/<int:id>')
def hero_by_id(id):
    hero = Hero.query.filter_by(id=id).first()

    hero_dict = {
        "name": hero.name,
        "age": hero.age,
       
    }

    response = make_response(
        jsonify(hero_dict),
        200
    )
    response.headers["Content-Type"] = "application/json"

    return response

@app.route('/power')
def power():
    
    powers =[]
    for power in Power.query.all():
        power_dict={

            "number_of_power":power.number_of_power,
            "description":power.description,
            
        }

        power.append(power_dict)
        response = make_response(
        jsonify(powers),
        200
    )
    response.headers["Content-Type"] = "application/json"

    return response

@app.route('/power/<int:id>')
def power_by_id(id):
    power = Power.query.filter_by(id=id).first()

    power_dict={
       "number_of_power":power.number_of_power,
       "description":power.description,
    }
    response = make_response(
        jsonify(game_dict),
        200
    )
    response.headers["Content-Type"] = "application/json"

    return response



@app.route('/power/int:id>' , methods=['GET', 'PATCH', 'DELETE'])
def power_by_id(id):
   if request.method =='GET':
       
       
     elif.request.method=='PATCH':
          power=Power.query.filter_by(id=id).first()
          for attr in request.form:
           setattr(power,attr,request.form.get(attr))

          db.session.add(power)
          db.session.commit()

        power-dict=power.to_dict()
        response = make_response(
                jsonify(review_dict),
                200
            )

            return response



       

    

