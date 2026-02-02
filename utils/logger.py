"""Logging infrastructure with file and stream handlers."""
import logging
import os
from datetime import datetime
from utils.config_parser import get_config

def setup_logger():
    """
    Set up application logger with file and stream handlers.
    Creates a log file with format: appname_YYYYMMDD_HHMMSS.log
    
    Returns:
        Configured logger instance
    """
    # Get configuration
    app_name = get_config('APP', 'app_name', 'FlaskApp')
    log_level = get_config('LOGGING', 'log_level', 'INFO')
    log_format = get_config('LOGGING', 'log_format', 
                           '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    log_directory = get_config('LOGGING', 'log_directory', 'logs')
    
    # Create logs directory if it doesn't exist
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)
    
    # Generate log filename with timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    safe_app_name = app_name.replace(' ', '_').lower()
    log_filename = f"{safe_app_name}_{timestamp}.log"
    log_path = os.path.join(log_directory, log_filename)
    
    # Create logger
    logger = logging.getLogger('flask_app')
    logger.setLevel(getattr(logging, log_level.upper(), logging.INFO))
    
    # Clear any existing handlers
    logger.handlers = []
    
    # Create formatters
    formatter = logging.Formatter(log_format)
    
    # File handler
    file_handler = logging.FileHandler(log_path, encoding='utf-8')
    file_handler.setLevel(getattr(logging, log_level.upper(), logging.INFO))
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    # Stream handler (console)
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(getattr(logging, log_level.upper(), logging.INFO))
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    
    logger.info(f"Logger initialized. Log file: {log_path}")
    
    return logger
