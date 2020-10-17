from flask import Flask

from .config import DevConfig

# Initializing application
app = Flask(__name__, instance_relative_config=True)  #allows connection to instance folder


# Setting up configuration 
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py') #connecting app with new config file

from app import views