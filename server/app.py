from flask import Flask
from flask import Flask, jsonify, request , make_response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 
from flask_restful import Api , Resource

from models import db,Hero,Power,HeroPower

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

Migrate = Migrate(app,db)

db.init_app(app)
api = Api(app)
class Home (Resource):
    def get(self):
        response_dict={"message ": 'this is my home page',           
       }
        response = make_response(response_dict,200,)
        return response
api.add_resource (Home,'/')       

        

@app.route('/heroes')
def heroes():
    heroes = []

    for hero in Hero.query.all():
        hero_dict = {
            "id": hero.id,
            "name": hero.name,
            "super_name": hero.super_name,
            "powers": [
                {'id':hp.power.id, 'name': hp.power.name, 'description': hp.power.description, 'strength': hp.strength} for hp in hero.hero_powers] 
                }  
        
        heroes.append(hero_dict)

    response = make_response(
    jsonify(heroes),
        200
    )
    return response  

   
@app.route('/heroes/<int:id>')
def hero_by_id(id):
    hero = Hero.query.filter_by(id=id).first()

    hero_dict = {
        "name": hero.name,
        "super_name": hero.super_name,
       
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

# @app.route('/power/<int:id>')
# def power_by_id(id):
#     power = Power.query.filter_by(id=id).first()

#     power_dict={
#        "number_of_power":power.number_of_power,
#        "description":power.description,
#     }
#     response = make_response(
#         jsonify(game_dict),
#         200
#     )
#     response.headers["Content-Type"] = "application/json"

#     return response
@app.route('/power/<int:id>', methods=['GET', 'PATCH'])
def power_by_id(id):
    if request.method == 'GET':
        power = Power.query.filter_by(id=id).first()

        power_dict={
        "name":power.name,
        "description":power.description,
        }
        response = make_response(
            jsonify(power_dict),
            200
        )
        response.headers["Content-Type"] = "application/json"

        return response
        

    elif request.method == 'PATCH':
        power = Power.query.get(id)

        if not power:
            return make_response(jsonify({"error": "Power not found"}), 404)

        for attr in request.form:
            setattr(power, attr, request.form.get(attr))

        db.session.add(power)
        db.session.commit()

        power = {
            "id":power.id,
            "name" :power.name,
            "description":power.description,

        }

        power_dict = power.to_dict(

        )
        response = make_response(jsonify(power_dict), 200)
        return response

    elif request.method == 'DELETE':
        # 
        pass

@app.route('/heropowers', methods=['GET', 'POST'])
def reviews():

    if request.method == 'GET':
        heropowers = []
        for heropower in HeroPower.query.all():
            heropower_dict = heropower.to_dict()
            heropowers.append(heropower_dict)

        heropower = make_response(
            jsonify(heropowers),
            200
        )

        return response

    elif request.method == 'POST':
        new_review = HeroPower(
            strength=request.form.get("strength"),
        )

        db.session.add(new_heropower)
        db.session.commit()

        heropower_dict = new_heropower.to_dict()

        response = make_response(
            jsonify(heropower_dict),
            201
        )

        return response
    
if __name__=='__main__':
    app.run(port=5555 ,debug=True)
    

