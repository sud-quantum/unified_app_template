"""
Test script to verify Flask app can be imported and basic structure is correct
"""
import sys
import os

print("=" * 60)
print("Flask App Structure Test")
print("=" * 60)
print()

# Test 1: Import config parser
print("Test 1: Importing config parser...")
try:
    from utils.config_parser import get_config
    print("✓ Config parser imported successfully")
    app_name = get_config('APP', 'app_name', 'Unknown')
    print(f"  App name from config: {app_name}")
except Exception as e:
    print(f"✗ Failed to import config parser: {e}")
    sys.exit(1)

print()

# Test 2: Import logger
print("Test 2: Importing logger...")
try:
    from utils.logger import setup_logger
    print("✓ Logger imported successfully")
except Exception as e:
    print(f"✗ Failed to import logger: {e}")
    sys.exit(1)

print()

# Test 3: Import database utilities
print("Test 3: Importing database utilities...")
try:
    from utils.database import init_db
    print("✓ Database utilities imported successfully")
except Exception as e:
    print(f"✗ Failed to import database: {e}")
    sys.exit(1)

print()

# Test 4: Import user model
print("Test 4: Importing user model...")
try:
    from models.user import create_user, verify_user
    print("✓ User model imported successfully")
except Exception as e:
    print(f"✗ Failed to import user model: {e}")
    sys.exit(1)

print()

# Test 5: Import forms
print("Test 5: Importing forms...")
try:
    from forms.auth_forms import LoginForm, RegistrationForm
    print("✓ Forms imported successfully")
except Exception as e:
    print(f"✗ Failed to import forms: {e}")
    print(f"  Note: This requires Flask-WTF to be installed")
    print(f"  Run: pip install Flask Flask-WTF WTForms email-validator")

print()

# Test 6: Import routes
print("Test 6: Importing routes...")
try:
    from routes.auth_routes import auth_bp
    from routes.main_routes import main_bp
    from routes.api_routes import api_bp
    print("✓ All route blueprints imported successfully")
except Exception as e:
    print(f"✗ Failed to import routes: {e}")

print()

# Test 7: Try to create Flask app
print("Test 7: Creating Flask app...")
try:
    from app import create_app
    flask_app = create_app()
    print("✓ Flask app created successfully")
    print(f"  App name: {flask_app.config.get('SECRET_KEY', 'Not set')[:20]}...")
except Exception as e:
    print(f"✗ Failed to create Flask app: {e}")
    print(f"  Note: Make sure all dependencies are installed")

print()
print("=" * 60)
print("Structure test complete!")
print("=" * 60)
print()
print("To run the app:")
print("1. Install dependencies: pip install -r requirements.txt")
print("2. Run: python app.py")
print("3. Visit: http://localhost:5000")
