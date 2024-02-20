import os
from views import *
from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATA_BASE")
db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run(debug=True)