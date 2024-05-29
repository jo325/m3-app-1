import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


def register_admin(self, **event_args):
  # Get the form data
  username = self.username_box.text
  email = self.email_box.text
  password = self.password_box.text

  # Add a new row to the Admins table
  new_row = app_tables.admins.add_row(username=username, email=email, password=password)

  # Display a success message or perform any additional actions
  print("Admin registered successfully!")
# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#
