from flask import Flask
from flask_blog.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

# creating instances
db= SQLAlchemy()
bcrypt=Bcrypt()
login_manager=LoginManager()
login_manager.login_view='users.login' #to secure pages login is function name of route
login_manager.login_message_category='info'

mail=Mail()



def create_app(config_class=Config):
    app = Flask(__name__)  # __name__ is the name of the module
    app.config.from_object(Config)  # configuring values from config.py

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from flask_blog.users.routes import users  # importing user instance
    from flask_blog.posts.routes import posts
    from flask_blog.main.routes import main
    from flask_blog.errors.handlers import errors

    app.register_blueprint(users)  # registering users
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app