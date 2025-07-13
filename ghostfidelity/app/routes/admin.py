from flask import Blueprint, request, session, redirect, url_for, flash
import os
from dotenv import load_dotenv

load_dotenv()

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/login-admin', methods=['POST'])
def login_admin():
    password = request.form.get('password')
    admin_password = os.getenv('ADMIN_PASSWORD')

    if password == admin_password:
        session['admin'] = True
        flash("Connexion administrateur réussie ✅", "success")
    else:
        session['admin'] = False
        flash("Mot de passe incorrect ❌", "error")

    return redirect(url_for('main.index'))

@admin_bp.route('/logout')
def logout():
    session.pop('admin', None)  # Supprime seulement "admin"
    flash("Vous avez été déconnecté avec succès.", "success")
    return redirect(url_for('main.index'))  # Ou 'index' selon ta route d'accueil
