from app import app
from flask_login import UserMixin

class User(db.Model, UserMixin)