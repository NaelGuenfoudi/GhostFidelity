from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

# Initialisation de l'extension SQLAlchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Chargement de la configuration à partir de config.py
    app.config.from_object(Config)
    
    # Initialisation de la base de données
    db.init_app(app)

    # Import des modèles pour s'assurer qu'ils sont enregistrés
    from .models import client

    # Création des tables (au besoin)
    with app.app_context():
        db.create_all()

    # Import des blueprints
    from .routes.main_bp import main_bp
    from .routes.admin import admin_bp

    from app.routes import main, client, admin

    app.register_blueprint(main_bp)
    app.register_blueprint(admin_bp)

    return app
