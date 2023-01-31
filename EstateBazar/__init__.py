from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)


    from .auth import auth
    from .adminauth import adminauth

    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(adminauth,url_prefix='/admin')

    from .models.user import User
    from .models.adminuser import AdminUser

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        if(id == 777):
            print("Admin-Login", int(id), id)
            return AdminUser.query.get(int(id))
        else:  
            print("User-Login", int(id), id) 
            return User.query.get(int(id))

    return app


def create_database(app):
    if not path.exists('EstateBazar/' + DB_NAME):
        # db.create_all(app=app)
        with app.app_context():
            db.create_all()
        print('Created Database!')
