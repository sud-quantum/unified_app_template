@echo off
REM Flask App Setup and Run Script
REM This script will set up and run your Flask application

echo ============================================================
echo Flask Boilerplate Template - Setup and Run
echo ============================================================
echo.

REM Check if virtual environment exists
if exist "venv\Scripts\activate.bat" (
    echo [1/4] Virtual environment found
) else (
    echo [1/4] Creating virtual environment...
    python -m venv venv
    if errorlevel 1 (
        echo ERROR: Failed to create virtual environment
        pause
        exit /b 1
    )
    echo Virtual environment created successfully
)

echo.
echo [2/4] Activating virtual environment...
call venv\Scripts\activate.bat

echo.
echo [3/4] Installing dependencies...
pip install Flask Flask-WTF WTForms email-validator Werkzeug
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)

echo.
echo [4/4] Starting Flask application...
echo.
echo ============================================================
echo Application starting...
echo Visit: http://localhost:5000
echo Press Ctrl+C to stop the server
echo ============================================================
echo.

python app.py

pause
