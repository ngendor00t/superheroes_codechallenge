from random import choice as rc

from faker import Faker

from app import app
from models import db, Hero, Power,HeroPower

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
    descriptions =['weak ','strong' , 'average']
    for n in range (15):
        power = power(number_of_powers=fake.number_of_powers(), description=rc(descriptions) )
        powers.append(power)

    db.session.add_all(powers)  


    heropowers=[]
    for n in range (10):
        heropower = HeroPower(strength =fake.strength())
        heropowers.append(hero)

    db.session.add_all(heropowers)  





   

