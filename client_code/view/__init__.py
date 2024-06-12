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
    self.items = items

    if not self.items:
      self.empty_cart_panel.visible = True

    
    self.repeating_panel_1.items = self.items
        
    
   
      
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('view_product')

  

  

    


    