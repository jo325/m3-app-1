from ._anvil_designer import register_formTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


class register_form(register_formTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def register_click(self, **event_args):
    """This method is called when the button is clicked"""
    username= self.Username_box.text
    email= self.email_box.text
    password= self.password_box.text

    anvil.server.call('register_form', username, email, password)
    Notification("Register submitted!").show()
  # Add a new row to the Admins table
   

  # Display a success message or perform any additional actions
    self.clear_inputs()
    print("Admin registered successfully!")
     
  def clear_inputs(self):
    # Clear our three text boxes
    self.Username_box.text = ""
    self.email_box.text = ""
    self.passward_box.text = ""