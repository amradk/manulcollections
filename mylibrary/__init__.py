from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from mylibrary import settings

app = Flask(__name__, template_folder='template') # create the application instance :)
app.config['SECRET_KEY']='HNdou238cxa03bHGAr'

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://"+settings.db['username']+':'+\
                        settings.db['password'] + '@' + settings.db['host'] +\
                        ':' + str(settings.db['port']) + '/' + settings.db['database'] +\
                        '?charset=' + settings.db['charset']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'False'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from mylibrary import routes, models
