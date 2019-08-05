from flask import Flask
from app.config import Config

#todo: recognize the moluldes made by me

app = Flask(__name__)
app.config.from_object(Config)

from app import routes

