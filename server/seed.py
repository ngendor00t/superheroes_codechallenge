from random import choice as rc

from faker import Faker

from app import app
from models import db, Hero, Power

db.init_app(app)

fake = Faker()
with app.app_context():

    Hero.query.delete()
    Power.query.delete()

    heroes =[]
    for n in range (10):
        hero = Hero(name = fake.name())
        heroes.append(hero)
        
    db.session.add_all(heroes)  

    powers = []



   

