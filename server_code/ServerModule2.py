import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.users
from anvil.tables import app_tables
from anvil.http import HttpError
from datetime import datetime, timezone

@anvil.server.route('/hello')
def say_hello():
    return "Hello from the Anvil server!"

@anvil.server.route('/greet/<name>')
def greet_user(name):
    return f"Greetings, {name}!"

@anvil.server.route('/login')
def login_user():
    # Access request headers to retrieve the forwarded user email
    headers = anvil.server.request.headers if hasattr(anvil.server, 'request') else {}
    email = None
    if headers:
        email = headers.get('X-Forwarded-User') or headers.get('x-forwarded-user')

    if not email or '@' not in email:
        raise HttpError(400, "Missing or invalid X-Forwarded-User header")

    # Get or create user row
    user_row = app_tables.users.get(email=email)
    if user_row is None:
        user_row = app_tables.users.add_row(email=email, created_at=str(datetime.now(timezone.utc)))

    # Force login for this user
    anvil.users.force_login(user_row)

    return email
