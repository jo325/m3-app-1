import anvil.email
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def register_form(username,email,password):
  # Get the form data
   
   app_tables.register.send_row(
    username=username, 
    email=email, 
    password=password 
  )
 
