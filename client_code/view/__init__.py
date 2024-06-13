from ._anvil_designer import viewTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class view(viewTemplate):
  def __init__(self,items, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.update_cart()

  def update_cart(self):
        cart_items = anvil.server.call('get_cart_items')
        self.repeating_panel_cart.items = cart_items
    
   
      
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('view_product')

  

  

    


    