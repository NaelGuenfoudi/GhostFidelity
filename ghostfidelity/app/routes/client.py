from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.models.client import Client, db
from app.routes.main_bp import main_bp
import qrcode
import io
import base64


# 🔍 Liste de tous les clients


# 📄 Page de détail d'un client - CORRECTION: utiliser string au lieu de uuid
@main_bp.route('/client/<string:uuid>', methods=['GET'])
def client_detail(uuid):
    client = Client.query.filter_by(uuid=uuid).first_or_404()

    # Récupère l'URL dynamique
    full_url = request.url_root.rstrip('/') + url_for('main.client_detail', uuid=client.uuid)

    # Génère le QR code
    qr_img = qrcode.make(full_url)
    buffered = io.BytesIO()
    qr_img.save(buffered, format="PNG")
    qr_base64 = base64.b64encode(buffered.getvalue()).decode()

    return render_template("client.html", client=client, qr_base64=qr_base64)



# ➕ Ajout d'une visite 
@main_bp.route('/client/<string:uuid>/add-coupe', methods=['POST'])
def add_coupe(uuid):
    if not session.get('admin'):
        flash("Accès réservé à l’administrateur.", "error")
        return redirect(url_for('main.index'))
    
    client = Client.query.filter_by(uuid=uuid).first_or_404()

    # Incrémentation de la visite
    client.nombre_visites += 1
    client.avancement_visite += 1

    if client.avancement_visite == 10:
        flash("🎉 Coupe offerte ! Le compteur fidélité est remis à zéro.", "success")
        client.avancement_visite = 0  # remise à zéro automatique

    db.session.commit()
    return redirect(url_for('main.client_detail', uuid=client.uuid))

# 📝 Mise à jour d'un client
@main_bp.route('/client/<string:uuid>/edit', methods=['GET', 'POST'])
def edit_client(uuid):
    return 0

# ❌ Suppression d'un client
@main_bp.route('/client/<string:uuid>/delete', methods=['POST'])
def delete_client(uuid):
    return 0

