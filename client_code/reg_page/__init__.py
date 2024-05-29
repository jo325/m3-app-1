from ._anvil_designer import reg_pageTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


class reg_page(reg_pageTemplate):
  def __init__(self, **properties):
    # Set Form Properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def register_click(self, **event_args):
    """This method is called when the button is clicked"""
    username= self.Username_box.text
    email= self.email_box.text
    password= self.password_box.text
    if not username or not email or not password:
            alert("All fields are required!")
            return
    success = anvil.server.call('register_form', username, email, password)
    if success:
      alert("Admin registered successfully!")
      open_form('Login')
    else:
      alert("Registration failed. Admin may already exist.")
    
    self.clear_inputs()
   
     
  def clear_inputs(self):
    # Clear our three text boxes
    self.Username_box.text = ""
    self.email_box.text = ""
    self.password_box.text = ""

  def login_s_click(self, **event_args):
    open_form('Login')
    """This method is called when the button is clicked"""
    
