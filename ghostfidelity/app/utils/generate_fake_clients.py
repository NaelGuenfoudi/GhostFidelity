# utils/generate_fake_clients.py

import uuid
import random
from datetime import date, timedelta
from faker import Faker
from app import create_app, db
from app.models.client import Client  # adapte selon ton arborescence

fake = Faker('fr_FR')

def generate_random_date(min_age=18, max_age=65):
    today = date.today()
    days = random.randint(min_age * 365, max_age * 365)
    return today - timedelta(days=days)

def generate_clients(n=15):
    app = create_app()
    with app.app_context():
        Client.query.delete()
        db.create_all()

        for _ in range(n):
            nombre_visites = random.randint(0, 30)
            avancement_visite = nombre_visites % 10

            filleuls = random.randint(0, 12)
            avancement_parrainage = filleuls % 3

            client = Client(
                uuid=str(uuid.uuid4()),
                prenom=fake.first_name(),
                nom=fake.last_name(),
                email=fake.unique.email(),
                birthday_date=generate_random_date(),
                nombre_visites=nombre_visites,
                avancement_visite=avancement_visite,
                filleuls=filleuls,
                avancement_parrainage=avancement_parrainage
            )

            db.session.add(client)

        db.session.commit()
        print(f"{n} clients générés avec succès.")

if __name__ == "__main__":
    generate_clients()
