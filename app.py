"""Main Flask application."""
from flask import Flask, render_template
from datetime import timedelta
import os

# Import utilities
from utils.config_parser import get_config, get_config_bool, get_config_int
from utils.logger import setup_logger
from utils.database import init_db

# Import blueprints
from routes.auth_routes import auth_bp
from routes.main_routes import main_bp
from routes.api_routes import api_bp

def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__)
    
    # Load configuration from config.ini
    app.config['SECRET_KEY'] = get_config('APP', 'secret_key', 'dev-secret-key-change-this')
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)
    
    # Initialize logger
    logger = setup_logger()
    logger.info("Starting Flask application")
    
    # Initialize database
    try:
        init_db()
        logger.info("Database initialized successfully")
    except Exception as e:
        logger.error(f"Database initialization failed: {str(e)}")
        raise
    
    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp)
    logger.info("Blueprints registered")
    
    # Error handlers
    @app.errorhandler(404)
    def not_found_error(error):
        logger.warning(f"404 error: {error}")
        return render_template('errors/404.html'), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        logger.error(f"500 error: {error}")
        return render_template('errors/500.html'), 500
    
    # Context processor for app name
    @app.context_processor
    def inject_app_name():
        return {
            'app_name': get_config('APP', 'app_name', 'Flask App')
        }
    
    return app

if __name__ == '__main__':
    app = create_app()
    
    # Get configuration
    debug = get_config_bool('APP', 'debug', True)
    host = get_config('APP', 'host', '0.0.0.0')
    port = get_config_int('APP', 'port', 5000)
    
    # Run application
    app.run(debug=debug, host=host, port=port)
