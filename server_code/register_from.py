import anvil.email
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import bcrypt

@anvil.server.callable
def register_form(username,email,password):
   if app_tables.admin.get(username=username) or app_tables.admin.get(email=email):
        return False

    # Hash the password before storing (using a library like bcrypt)
   hashed_password = hash_password(password)  # You'll need to implement this function

    # Insert the new admin into the table
   app_tables.admin.add_row(username=username, email=email, password=hashed_password)
   return True

def hash_password(password):
    import bcrypt
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

@anvil.server.callable
def Login_admin(username_or_email, password):
    # Fetch the admin record by username or email
    admin_record = app_tables.admin.get(username=username_or_email) or app_tables.admin.get(email=username_or_email)

    if admin_record and check_password(password, admin_record['password']):
        return True  # Login successful
    return False  # Login failed

def hash_password2(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

def check_password(password, hashed):
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))
 
