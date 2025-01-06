import os

# The database configuration (PostgreSQL)
SQLALCHEMY_DATABASE_URI = os.getenv(
    'DATABASE_URL',
    'postgresql://your_username:your_password@localhost:5432/your_database'
)

SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')