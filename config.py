import os

SECRET_KEY = 'jogoteca'

UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'

SQLALCHEMY_DATABASE_URI = os.getenv("DATA_BASE")