# Flask Application Boilerplate Template

A comprehensive, reusable Flask application template with modern UI, authentication, and configuration management. Perfect for quickly starting new Flask projects with a professional foundation.

## Features

✨ **Authentication System**
- User registration and login with Flask-WTF forms
- Secure password hashing with Werkzeug
- Session management with "Remember Me" functionality
- Login required decorator for protected routes

🎨 **Modern UI**
- Bootstrap 5 with custom corporate theme
- Light and dark mode switching with localStorage persistence
- Responsive design for all screen sizes
- Toast notifications (success, error, warning, info)
- Breadcrumb navigation
- Custom error pages (404, 500)

⚙️ **Configuration Management**
- Centralized `config.ini` file for all settings
- Easy configuration parsing utilities
- Separate settings for app, database, and logging

📊 **Database**
- SQLite database with user management
- Clean database abstraction layer
- Helper functions for common operations

📝 **Logging**
- File handler with timestamped log files (`appname_YYYYMMDD_HHMMSS.log`)
- Stream handler for console output
- Configurable log levels and formats
- Automatic log directory creation

🏗️ **Architecture**
- Modular structure with blueprints
- Separate files for routes and API endpoints
- Function-based approach (no classes)
- Clean separation of concerns

## Project Structure

```
flask_app/
├── app.py                      # Main application file
├── config.ini                  # Configuration file
├── requirements.txt            # Python dependencies
├── forms/
│   └── auth_forms.py          # Authentication forms
├── models/
│   └── user.py                # User model
├── routes/
│   ├── auth_routes.py         # Authentication routes
│   ├── main_routes.py         # Main application routes
│   └── api_routes.py          # API endpoints
├── static/
│   ├── css/
│   │   └── custom.css         # Custom styles
│   └── js/
│       ├── theme.js           # Theme switching
│       └── toast.js           # Toast notifications
├── templates/
│   ├── base.html              # Base template
│   ├── index.html             # Home page
│   ├── about.html             # About page
│   ├── auth/
│   │   ├── login.html         # Login page
│   │   └── register.html      # Registration page
│   └── errors/
│       ├── 404.html           # 404 error page
│       └── 500.html           # 500 error page
└── utils/
    ├── config_parser.py       # Configuration utilities
    ├── database.py            # Database utilities
    └── logger.py              # Logging setup
```

## Installation

1. **Clone or copy this template to your project directory**

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - Linux/Mac:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Configure the application**
   - Edit `config.ini` to customize:
     - App name
     - Secret key (change for production!)
     - Database path
     - Logging settings

6. **Run the application**
   ```bash
   python app.py
   ```

7. **Access the application**
   - Open your browser and navigate to: `http://localhost:5000`

## Configuration

All configuration is managed through `config.ini`:

### [APP]
- `app_name`: Your application name
- `secret_key`: Flask secret key (change in production!)
- `debug`: Enable/disable debug mode
- `host`: Server host (default: 0.0.0.0)
- `port`: Server port (default: 5000)

### [DATABASE]
- `database_path`: SQLite database file path

### [LOGGING]
- `log_level`: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
- `log_format`: Log message format
- `log_directory`: Directory for log files

## Usage

### User Registration
1. Navigate to `/register`
2. Enter username and password
3. Submit the form
4. You'll be redirected to login

### User Login
1. Navigate to `/login`
2. Enter credentials
3. Optionally check "Remember Me"
4. Access protected routes

### Theme Switching
- Click the sun/moon icon in the header
- Theme preference is saved in localStorage
- Persists across page reloads

### Toast Notifications
Use the global JavaScript functions:
```javascript
showToast('Message', 'success');  // or 'error', 'warning', 'info'
showSuccess('Success message');
showError('Error message');
showWarning('Warning message');
showInfo('Info message');
```

### Adding New Routes
1. Create route functions in `routes/main_routes.py` or create a new blueprint
2. Use the `@login_required` decorator for protected routes
3. Register new blueprints in `app.py`

### Adding API Endpoints
1. Add new routes to `routes/api_routes.py`
2. Return JSON responses using `jsonify()`
3. Include proper error handling

## Customization

### Changing Colors
Edit `static/css/custom.css` and modify the CSS variables in `:root` and `[data-bs-theme="dark"]`

### Adding Pages
1. Create a new template in `templates/`
2. Add a route in `routes/main_routes.py`
3. Include breadcrumb data in the render_template call

### Database Schema
Modify `utils/database.py` to add new tables or change the schema

## Security Notes

⚠️ **Important**: Before deploying to production:
1. Change the `secret_key` in `config.ini` to a strong, random value
2. Set `debug = False` in `config.ini`
3. Use environment variables for sensitive data
4. Configure proper database backups
5. Use HTTPS in production
6. Review and update security settings

## Technologies Used

- **Backend**: Flask 3.0.0
- **Forms**: Flask-WTF, WTForms
- **Database**: SQLite
- **Frontend**: Bootstrap 5.3.2, JavaScript
- **Icons**: Bootstrap Icons
- **Security**: Werkzeug password hashing

## License

This template is free to use for any project.

## Support

For issues or questions, refer to the Flask documentation:
- Flask: https://flask.palletsprojects.com/
- Flask-WTF: https://flask-wtf.readthedocs.io/
- Bootstrap: https://getbootstrap.com/

---

**Happy Coding! 🚀**
