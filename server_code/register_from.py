import anvil.email
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def register_form(username,email,password):
  # Get the form data
   anvil.email.send(to="noreply@gmail.com", # Change this to your email address!
                   subject=f"register from {username}",
                   text=f""" 
   A new person has filled out the register form!

   Name: {username}
   Email address: {email}
   password:
   {password}
   """)
   app_tables.register.send_row(
    username=username, 
    email=email, 
    password=password, 
    
  )
 
