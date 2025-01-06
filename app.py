from flask import Flask
from views.views import views_blueprint
from models import db
from dotenv import load_dotenv
import os

def create_app():
    # Loading the enviroment variables
    load_dotenv()

    # Creating the Flask app
    app = Flask(__name__)

    # Load configurations
    app.config.from_pyfile('config.py')

    # Initialize database
    db.init_app(app)

    # Register the blueprints
    app.register_blueprint(views_blueprint)
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=8080)