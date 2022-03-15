from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "vehicle.db"

def create_app():
    
    appNEW = Flask(__name__)
    appNEW.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    appNEW.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(appNEW)
    
    from views import views
    from models import models
    
    appNEW.register_blueprint(views, url_prefix='/')
    appNEW.register_blueprint(models,url_prefix='/')

    create_database(appNEW)
    
    return appNEW

vehicles = []


def create_database(appNEW):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=appNEW)
        print('Created Database!')
        



    


    
