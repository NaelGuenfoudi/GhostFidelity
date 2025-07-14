# app/routes/main.py

from flask import  render_template
from app.routes.main_bp import main_bp


@main_bp.route('/')
def index():
    return render_template('index.html')
