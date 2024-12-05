from flask import Flask
from app.config import Config
from app.extensions import db, cache  # Import from extensions instead

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    cache.init_app(app)

    # Import routes after initializing extensions to avoid circular imports
    from app.routes.api import api
    from app.routes.main import main
    
    app.register_blueprint(main)
    app.register_blueprint(api, url_prefix='/api')

    return app
