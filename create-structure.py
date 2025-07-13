import os

folders = [
    "ghostfidelity/app/routes",
    "ghostfidelity/app/models",
    "ghostfidelity/app/templates",
    "ghostfidelity/app/static/css",
    "ghostfidelity/app/static/js",
    "ghostfidelity/app/static/images",
    "ghostfidelity/app/utils",
    "ghostfidelity/instance",
]

files = {
    "ghostfidelity/app/__init__.py": "",
    "ghostfidelity/app/routes/__init__.py": "",
    "ghostfidelity/app/routes/client.py": "",
    "ghostfidelity/app/routes/admin.py": "",
    "ghostfidelity/app/routes/main.py": "",
    "ghostfidelity/app/routes/scan.py": "",
    "ghostfidelity/app/models/__init__.py": "",
    "ghostfidelity/app/models/client.py": "",
    "ghostfidelity/app/templates/base.html": "<!-- Base HTML Template -->",
    "ghostfidelity/app/templates/index.html": "<!-- Home Page -->",
    "ghostfidelity/app/templates/client.html": "<!-- Client Page -->",
    "ghostfidelity/app/templates/admin_dashboard.html": "<!-- Admin Dashboard -->",
    "ghostfidelity/app/templates/create_client.html": "<!-- Create Client Page -->",
    "ghostfidelity/app/templates/scan.html": "<!-- QR Scan Page -->",
    "ghostfidelity/app/utils/__init__.py": "",
    "ghostfidelity/app/utils/auth.py": "# Admin authentication logic here",
    "ghostfidelity/app/utils/qrcode_tools.py": "# QR code generation and reading tools",
    "ghostfidelity/instance/config.py": "# Instance-specific config (e.g., secrets)",
    "ghostfidelity/config.py": "# Global configuration settings",
    "ghostfidelity/run.py": "from app import create_app\n\napp = create_app()\n\nif __name__ == '__main__':\n    app.run(debug=True)",
    "ghostfidelity/requirements.txt": "flask\npython-dotenv\nqrcode\nflask_sqlalchemy\nflask_migrate\n",
    "ghostfidelity/.env": "FLASK_APP=run.py\nFLASK_ENV=development\nSECRET_KEY=your_secret_key\n",
    "ghostfidelity/.gitignore": "*.pyc\n__pycache__/\ninstance/\n.env\n",
}

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create files
for path, content in files.items():
    with open(path, "w") as f:
        f.write(content)

print("✅ Structure Flask 'ghostfidelity' générée avec succès.")
