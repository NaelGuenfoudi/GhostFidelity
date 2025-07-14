from flask import render_template, Blueprint, request, session, redirect, url_for, flash
import os
import uuid
from datetime import datetime
from dotenv import load_dotenv
from app import db
from app.models.client import Client
from sqlalchemy import func


load_dotenv()

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/login-admin', methods=['POST'])
def login_admin():
    password = request.form.get('password')
    admin_password = os.getenv('ADMIN_PASSWORD')

    if password == admin_password:
        session['admin'] = True
        flash("Connexion administrateur réussie ✅", "success")
        return redirect(url_for('admin.dashboard'))  # Redirection vers le dashboard
    else:
        session['admin'] = False
        flash("Mot de passe incorrect ❌", "error")
        return redirect(url_for('main.index'))  # Redirection vers la page d'accueil si échec


@admin_bp.route('/logout')
def logout():
    session.pop('admin', None)  # Supprime seulement "admin"
    flash("Vous avez été déconnecté avec succès.", "success")
    return redirect(url_for('main.index'))  # Ou 'index' selon ta route d'accueil

@admin_bp.route('/dashboard')
def dashboard():
    if not session.get('admin'):
        flash("Accès réservé à l’administrateur.", "error")
        return redirect(url_for('main.index'))

    visites_total = db.session.query(func.sum(Client.nombre_visites)).scalar() or 0
    
    stats = {
        "visites_total": visites_total,
        "coupes_offertes": 34  # valeur temporaire
    }

    clients = Client.query.all()


    return render_template("admin/dashboard.html", stats=stats, clients=clients)


@admin_bp.route('/client/create', methods=['GET', 'POST'])
def create_client():
   
    if not session.get('admin'):
        flash("Accès réservé à l’administrateur.", "error")
        return redirect(url_for('main.index'))

    if request.method == 'POST':
        nom = request.form.get('nom')
        prenom = request.form.get('prenom')
        email = request.form.get('email')
        birthday_str = request.form.get('birthday_date')  # format yyyy-mm-dd

        if not nom or not prenom or not email or not birthday_str:
            flash("Tous les champs sont requis.", "error")
            return redirect(request.url)

        try:
            birthday_date = datetime.strptime(birthday_str, "%Y-%m-%d").date()
        except ValueError:
            flash("Format de date invalide. Utilisez AAAA-MM-JJ.", "error")
            return redirect(request.url)

        nouveau_client = Client(
            uuid=str(uuid.uuid4()),
            nom=nom,
            prenom=prenom,
            email=email,
            birthday_date=birthday_date,
            nombre_visites=0,
            avancement_visite=0,
            filleuls=0,
            avancement_parrainage=0
        )

        db.session.add(nouveau_client)
        db.session.commit()
        flash("Client créé avec succès ✅", "success")
        return redirect(url_for('main.client_detail', uuid=nouveau_client.uuid))

    return render_template("admin/create_client.html")
