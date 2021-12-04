from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

application = Flask(__name__) #original tutorial was "app =" but AWS ElasticBeanstalk needs "application ="
app = application
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models #app here is the name of the folder (also called "package")
