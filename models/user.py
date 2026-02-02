"""User model with authentication functions."""
from werkzeug.security import generate_password_hash, check_password_hash
from utils.database import execute_query
import logging

logger = logging.getLogger('flask_app')

def create_user(username, password):
    """
    Create a new user with hashed password.
    
    Args:
        username: User's username
        password: User's plain text password
        
    Returns:
        User ID if successful, None if username already exists
    """
    try:
        password_hash = generate_password_hash(password)
        query = "INSERT INTO users (username, password_hash) VALUES (?, ?)"
        user_id = execute_query(query, (username, password_hash), commit=True)
        logger.info(f"User created: {username}")
        return user_id
    except Exception as e:
        logger.error(f"Error creating user {username}: {str(e)}")
        return None

def get_user_by_username(username):
    """
    Get user by username.
    
    Args:
        username: User's username
        
    Returns:
        User row or None
    """
    query = "SELECT * FROM users WHERE username = ?"
    return execute_query(query, (username,), fetch_one=True)

def verify_user(username, password):
    """
    Verify user credentials.
    
    Args:
        username: User's username
        password: User's plain text password
        
    Returns:
        User row if credentials are valid, None otherwise
    """
    user = get_user_by_username(username)
    if user and check_password_hash(user['password_hash'], password):
        logger.info(f"User authenticated: {username}")
        return user
    logger.warning(f"Failed authentication attempt for: {username}")
    return None

def get_user_by_id(user_id):
    """
    Get user by ID.
    
    Args:
        user_id: User's ID
        
    Returns:
        User row or None
    """
    query = "SELECT * FROM users WHERE id = ?"
    return execute_query(query, (user_id,), fetch_one=True)
