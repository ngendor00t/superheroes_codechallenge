from flask import Flask
from flask import Flask, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from models import db,Hero,Power,HeroPower

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

Migrate = Migrate(app,db)

db.init_app(app)

# @app.route('/heroes')
# def heroes():




# if __name__ == '__main__':
#     app.run(port=5555)