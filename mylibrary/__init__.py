from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import mylibrary.settings

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app =  Flask(__name__, template_folder='template') # create the application instance :)
    app.config['SECRET_KEY'] = 'HNdou238cxa03bHGAr'

    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://" + settings.db['username'] + ':' + \
                                            settings.db['password'] + '@' + settings.db['host'] + \
                                            ':' + str(settings.db['port']) + '/' + settings.db['database'] + \
                                            '?charset=' + settings.db['charset']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'False'

    from . import root
    from . import book
    from . import author
    from . import genre
    from . import api

    app.register_blueprint(root.bp)
    app.register_blueprint(book.bp)
    app.register_blueprint(author.bp)
    app.register_blueprint(genre.bp)
    app.register_blueprint(api.bp)

    db.init_app(app)
    migrate.init_app(app, db)

    return app

from mylibrary import models
