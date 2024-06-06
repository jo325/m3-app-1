from ._anvil_designer import LoginTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


class Login(LoginTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def login_click(self, **event_args):
    username_or_email = self.username_or_email_textbox.text
    password = self.password_textbox.text

    if not username_or_email or not password:
      alert("Both fields are required!")
      return

    success = anvil.server.call('Login_admin', username_or_email, password)

    if success:
       alert("Login successful!")
            # Navigate to the admin dashboard or main page
       open_form('main')  # Replace 'MainPage' with your main form
    else:
        alert("Login failed. Please check your credentials.")
    """This method is called when the button is clicked"""
   
