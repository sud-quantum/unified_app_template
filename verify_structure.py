"""
Quick verification script to test the Flask app structure
"""
import os
import sys

def check_file_exists(path, description):
    """Check if a file exists and print result."""
    exists = os.path.exists(path)
    status = "✓" if exists else "✗"
    print(f"{status} {description}: {path}")
    return exists

def main():
    print("=" * 60)
    print("Flask Boilerplate Template - Structure Verification")
    print("=" * 60)
    print()
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    all_good = True
    
    # Check core files
    print("Core Files:")
    all_good &= check_file_exists(os.path.join(base_dir, "app.py"), "Main application")
    all_good &= check_file_exists(os.path.join(base_dir, "config.ini"), "Configuration")
    all_good &= check_file_exists(os.path.join(base_dir, "requirements.txt"), "Requirements")
    print()
    
    # Check utilities
    print("Utilities:")
    all_good &= check_file_exists(os.path.join(base_dir, "utils", "config_parser.py"), "Config parser")
    all_good &= check_file_exists(os.path.join(base_dir, "utils", "logger.py"), "Logger")
    all_good &= check_file_exists(os.path.join(base_dir, "utils", "database.py"), "Database utils")
    print()
    
    # Check models
    print("Models:")
    all_good &= check_file_exists(os.path.join(base_dir, "models", "user.py"), "User model")
    print()
    
    # Check forms
    print("Forms:")
    all_good &= check_file_exists(os.path.join(base_dir, "forms", "auth_forms.py"), "Auth forms")
    print()
    
    # Check routes
    print("Routes:")
    all_good &= check_file_exists(os.path.join(base_dir, "routes", "auth_routes.py"), "Auth routes")
    all_good &= check_file_exists(os.path.join(base_dir, "routes", "main_routes.py"), "Main routes")
    all_good &= check_file_exists(os.path.join(base_dir, "routes", "api_routes.py"), "API routes")
    print()
    
    # Check templates
    print("Templates:")
    all_good &= check_file_exists(os.path.join(base_dir, "templates", "base.html"), "Base template")
    all_good &= check_file_exists(os.path.join(base_dir, "templates", "index.html"), "Index page")
    all_good &= check_file_exists(os.path.join(base_dir, "templates", "about.html"), "About page")
    all_good &= check_file_exists(os.path.join(base_dir, "templates", "auth", "login.html"), "Login page")
    all_good &= check_file_exists(os.path.join(base_dir, "templates", "auth", "register.html"), "Register page")
    all_good &= check_file_exists(os.path.join(base_dir, "templates", "errors", "404.html"), "404 page")
    all_good &= check_file_exists(os.path.join(base_dir, "templates", "errors", "500.html"), "500 page")
    print()
    
    # Check static files
    print("Static Files:")
    all_good &= check_file_exists(os.path.join(base_dir, "static", "css", "custom.css"), "Custom CSS")
    all_good &= check_file_exists(os.path.join(base_dir, "static", "js", "theme.js"), "Theme JS")
    all_good &= check_file_exists(os.path.join(base_dir, "static", "js", "toast.js"), "Toast JS")
    print()
    
    print("=" * 60)
    if all_good:
        print("✓ All files present! Structure verification PASSED")
    else:
        print("✗ Some files missing! Structure verification FAILED")
    print("=" * 60)
    
    return 0 if all_good else 1

if __name__ == "__main__":
    sys.exit(main())
