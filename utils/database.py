"""Database initialization and helper functions."""
import sqlite3
import os
from utils.config_parser import get_config

def get_db_path():
    """Get the database path from config."""
    return get_config('DATABASE', 'database_path', 'instance/users.db')

def init_db():
    """
    Initialize the SQLite database and create tables if they don't exist.
    Creates the instance directory if needed.
    """
    db_path = get_db_path()
    
    # Create instance directory if it doesn't exist
    db_dir = os.path.dirname(db_path)
    if db_dir and not os.path.exists(db_dir):
        os.makedirs(db_dir)
    
    # Connect to database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Create users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()

def get_db_connection():
    """
    Get a database connection.
    
    Returns:
        SQLite connection object
    """
    db_path = get_db_path()
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

def execute_query(query, params=None, fetch_one=False, fetch_all=False, commit=False):
    """
    Execute a database query with error handling.
    
    Args:
        query: SQL query string
        params: Query parameters (tuple or dict)
        fetch_one: Return single row
        fetch_all: Return all rows
        commit: Commit the transaction
        
    Returns:
        Query results or None
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        
        result = None
        if fetch_one:
            result = cursor.fetchone()
        elif fetch_all:
            result = cursor.fetchall()
        
        if commit:
            conn.commit()
            result = cursor.lastrowid
        
        return result
    except sqlite3.Error as e:
        conn.rollback()
        raise e
    finally:
        conn.close()
