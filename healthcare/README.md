# Healthcare Django Project (Scaffold)

This is a minimal, ready-to-run Django project scaffold for a healthcare web app that includes:

- User authentication (signup/login/logout)
- Pages: Home, About, Add Info (for adding patient or general info)
- Basic UI/UX using plain CSS (keeps dependencies minimal)
- SQLite DB (Django default)

How to run:

1. Create and activate a Python virtualenv:
   ```bash
   python -m venv venv
   source venv/bin/activate      # macOS / Linux
   venv\Scripts\activate       # Windows PowerShell
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run migrations and create a superuser:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

4. Run the dev server:
   ```bash
   python manage.py runserver
   ```

Visit http://127.0.0.1:8000

This scaffold includes example templates and simple CSS for decent UI/UX. Customize as needed.
