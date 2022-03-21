from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


db = SQLAlchemy(app)

from flask_migrate import Migrate 
migrate = Migrate(app,db)

app.config.from_object(Config)
from app import views