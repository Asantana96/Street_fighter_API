#import flask library that we downloaded in the terminal (view in requirements)
from flask import Flask 

#makes an instance of our flask library 
app = Flask(__name__)


from app.blueprints.auth import bp as auth_bp
app.register_blueprint(auth_bp)

from app.blueprints.main import bp as main_bp
app.register_blueprint(main_bp)

