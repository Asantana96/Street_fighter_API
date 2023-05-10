#import flask library that we downloaded in the terminal (view in requirements)
from flask import Flask 
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
#makes an instance of our flask library 
app = Flask(__name__)
app.config.from_object(Config)
db= SQLAlchemy(app)
migrate = Migrate(app,db)

from app.blueprints.auth import bp as auth_bp
app.register_blueprint(auth_bp)

from app.blueprints.main import bp as main_bp
app.register_blueprint(main_bp)

from app import models

