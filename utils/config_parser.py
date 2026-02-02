"""Configuration parser module for reading config.ini settings."""
import configparser
import os

# Get the path to config.ini
config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config.ini')

# Create config parser
config = configparser.ConfigParser()
config.read(config_path)

def get_config(section, key, fallback=None):
    """
    Get a configuration value from config.ini.
    
    Args:
        section: The section name in config.ini
        key: The key name within the section
        fallback: Default value if key is not found
        
    Returns:
        The configuration value or fallback
    """
    try:
        return config.get(section, key)
    except (configparser.NoSectionError, configparser.NoOptionError):
        return fallback

def get_config_bool(section, key, fallback=False):
    """
    Get a boolean configuration value from config.ini.
    
    Args:
        section: The section name in config.ini
        key: The key name within the section
        fallback: Default value if key is not found
        
    Returns:
        The boolean configuration value or fallback
    """
    try:
        return config.getboolean(section, key)
    except (configparser.NoSectionError, configparser.NoOptionError):
        return fallback

def get_config_int(section, key, fallback=0):
    """
    Get an integer configuration value from config.ini.
    
    Args:
        section: The section name in config.ini
        key: The key name within the section
        fallback: Default value if key is not found
        
    Returns:
        The integer configuration value or fallback
    """
    try:
        return config.getint(section, key)
    except (configparser.NoSectionError, configparser.NoOptionError):
        return fallback
