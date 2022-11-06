import os
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, static_folder=None)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['JSON_AS_ASCII'] = False
db = SQLAlchemy(app)


CORS(app)


from app.orders import orders
app.register_blueprint(orders, url_prefix='/orders')

from app.services import services
app.register_blueprint(services, url_prefix='/services')

from app.cabins import cabins
app.register_blueprint(cabins, url_prefix='/cabins')
