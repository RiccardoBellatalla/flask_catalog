from flask import Flask
application = Flask(__name__) #original tutorial was "app =" but AWS ElasticBeanstalk needs "application ="

from app import routes #app here is the name of the folder (also called "package")
