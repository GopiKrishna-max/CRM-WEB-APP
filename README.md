# Django CRM - Minimal Example

This is a minimal Django CRM example project suitable for learning and quick prototyping.

## What's included
- Django project `crm_project`
- App `crm` with models `Contact` and `Deal`
- Basic CRUD views for Contacts
- Simple templates (Tailwind-like minimal styling)
- `requirements.txt`

## How to run
1. Create a virtualenv and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate   # on Windows: venv\Scripts\activate
   ```
2. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
3. Apply migrations and run server:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```
4. Visit `http://127.0.0.1:8000/contacts/`

NOTE: This is a minimal example for educational purposes. For production use, secure the SECRET_KEY, DEBUG, and static file handling.


## Authentication
- This update adds login, logout (Django built-in) and signup (UserCreationForm).
- Login URL: /accounts/login/  — Logout: /accounts/logout/ — Signup: /accounts/signup/ or /signup/
- After signup/login users are redirected to /contacts/.

Create a superuser with `python manage.py createsuperuser` to access the admin.


## Dashboard
- The home page `/` now shows a Bootstrap dashboard with total contacts, deals, and recent contacts.
