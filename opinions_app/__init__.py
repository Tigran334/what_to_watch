from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('settings.Config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Импорты модулей приложения — САМЫМИ ПОСЛЕДНИМИ!
from . import views, models, error_handlers, cli_commands