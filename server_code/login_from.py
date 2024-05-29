import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


def login_admin(self, **event_args):
  # Get the form data
  email = self.email_box.text
  password = self.password_box.text

  # Search the Admins table for a matching email and password
  query = (app_tables.register.email == email) & (app_tables.register.password == password)
  matching_rows = app_tables.register.search(query)

  if matching_rows:
    # Admin is valid, perform any additional actions (e.g., redirect to admin dashboard)
    print("Admin logged in successfully!")
  else:
    # Admin is invalid, display an error message
    print("Invalid email or password.")

