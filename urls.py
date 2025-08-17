# Flask doesn't use urls.py, but if you use blueprints:
from app import app
from views import main

app.register_blueprint(main)
