# Imports
from flask import Flask

# Config
app = Flask(__name__)
print(app)
from . import views
