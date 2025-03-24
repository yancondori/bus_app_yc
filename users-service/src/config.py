import os

class Config:
    DEBUG = True  # Set to False in production
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'  # Important for security
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///users.db' # Use environment variable for production
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Reduces overhead
