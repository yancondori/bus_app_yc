from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
from extensions import db  
from config import Config
from routes import users_bp

#db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    app.register_blueprint(users_bp)

    with app.app_context():
        db.create_all()  # Create tables if they don't exist

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)

