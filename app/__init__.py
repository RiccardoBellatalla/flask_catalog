from flask import Flask
from config import Config

application = Flask(__name__) #original tutorial was "app =" but AWS ElasticBeanstalk needs "application ="
app = application
app.config.from_object(Config)

from app import routes #app here is the name of the folder (also called "package")
