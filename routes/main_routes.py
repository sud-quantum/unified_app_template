"""Main application routes."""
from flask import Blueprint, render_template, redirect, url_for, session, request
from functools import wraps
import logging

logger = logging.getLogger('flask_app')

main_bp = Blueprint('main', __name__)

def login_required(f):
    """Decorator to require login for routes."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('auth.login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

@main_bp.route('/')
@login_required
def index():
    """Home page route."""
    username = session.get('username', 'User')
    return render_template('index.html', 
                         username=username,
                         breadcrumb=[
                             {'text': 'Home', 'url': None}
                         ])

@main_bp.route('/about')
def about():
    """About page route."""
    return render_template('about.html',
                         breadcrumb=[
                             {'text': 'Home', 'url': url_for('main.index')},
                             {'text': 'About', 'url': None}
                         ])
