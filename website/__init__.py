from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():

    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'martiaisthesmartesthumanalive'

    
    from .views import views
    from .auth import auth


    app.register_blueprint(auth, url_perefix='/')
    app.register_blueprint(views,   url_perefix='/')
    
  

    return app
