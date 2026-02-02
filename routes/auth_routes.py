"""Authentication routes for login, registration, and logout."""
from flask import Blueprint, render_template, redirect, url_for, flash, session, request
from forms.auth_forms import RegistrationForm, LoginForm
from models.user import create_user, verify_user
import logging

logger = logging.getLogger('flask_app')

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    """User registration route."""
    # Redirect if already logged in
    if 'user_id' in session:
        return redirect(url_for('main.index'))
    
    form = RegistrationForm()
    
    if form.validate_on_submit():
        try:
            user_id = create_user(form.username.data, form.password.data)
            if user_id:
                flash('Registration successful! Please log in.', 'success')
                logger.info(f"New user registered: {form.username.data}")
                return redirect(url_for('auth.login'))
            else:
                flash('Registration failed. Please try again.', 'error')
                logger.error(f"Registration failed for: {form.username.data}")
        except Exception as e:
            flash('An error occurred during registration.', 'error')
            logger.error(f"Registration error: {str(e)}")
    
    return render_template('auth/register.html', form=form, breadcrumb=[
        {'text': 'Home', 'url': url_for('main.index')},
        {'text': 'Register', 'url': None}
    ])

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """User login route."""
    # Redirect if already logged in
    if 'user_id' in session:
        return redirect(url_for('main.index'))
    
    form = LoginForm()
    
    if form.validate_on_submit():
        user = verify_user(form.username.data, form.password.data)
        if user:
            session['user_id'] = user['id']
            session['username'] = user['username']
            session.permanent = form.remember.data
            flash('Login successful!', 'success')
            logger.info(f"User logged in: {user['username']}")
            
            # Redirect to next page or home
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.index'))
        else:
            flash('Invalid username or password.', 'error')
            logger.warning(f"Failed login attempt for: {form.username.data}")
    
    return render_template('auth/login.html', form=form, breadcrumb=[
        {'text': 'Home', 'url': url_for('main.index')},
        {'text': 'Login', 'url': None}
    ])

@auth_bp.route('/logout')
def logout():
    """User logout route."""
    username = session.get('username', 'Unknown')
    session.clear()
    flash('You have been logged out.', 'info')
    logger.info(f"User logged out: {username}")
    return redirect(url_for('auth.login'))
