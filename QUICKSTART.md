# Quick Start Guide

## Get Started in 3 Steps

### Step 1: Install Dependencies

```bash
# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# Install requirements
pip install -r requirements.txt
```

### Step 2: Configure (Optional)

Edit `config.ini` to customize:
- App name
- Secret key (important for production!)
- Database path
- Logging settings

### Step 3: Run

```bash
python app.py
```

Visit: **http://localhost:5000**

## First Time Usage

1. **Register**: Go to `/register` and create an account
2. **Login**: Use your credentials to login
3. **Explore**: Check out the home page and test features
4. **Try Theme Toggle**: Click the sun/moon icon in the header
5. **Test Toasts**: Click the notification demo buttons on the home page

## Project Structure at a Glance

```
flask_app/
├── app.py              # Start here - main application
├── config.ini          # Configure here - all settings
├── routes/             # Add routes here
├── templates/          # Add pages here
├── static/             # Add CSS/JS here
├── models/             # Add models here
└── utils/              # Helper functions
```

## Common Tasks

### Change App Name
Edit `config.ini` → `app_name = Your Name`

### Change Colors
Edit `static/css/custom.css` → Modify CSS variables

### Add a New Page
1. Create `templates/mypage.html`
2. Add route in `routes/main_routes.py`

### Add API Endpoint
Add route in `routes/api_routes.py`

## Need Help?

- Check `README.md` for detailed documentation
- Review `walkthrough.md` for implementation details
- All code is well-commented

## Production Deployment

⚠️ **Before going live:**
1. Change `secret_key` in config.ini
2. Set `debug = False`
3. Use a production server (Gunicorn, etc.)
4. Enable HTTPS

---

**Happy coding! 🚀**
