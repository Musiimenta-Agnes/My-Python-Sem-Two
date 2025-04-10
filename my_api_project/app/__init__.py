
from flask import Flask
from app.extensions import migrate,jwt
from app.extensions import db

# Ensure to import the blueprint to work with it.
from app.controllers.auth.auth_controller import auth




#Define the appliction factory function
def create_app():


    #Defining the app instance
    app = Flask(__name__)

    
    #Accessing the app
    app.config.from_object("config.Config")

    #Register our database instance within our application file
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)



    #Register models from the appliation file.
    from app.models.user_model import User
    from app.models.book_model import Book

    # Registering the blueprints
    app.register_blueprint(auth)





#Make our app decorator
    @app.route("/")

    def home():
        return "Am doing python"
    


    return app