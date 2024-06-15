from ._anvil_designer import viewTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..view_product import view_product

class view(viewTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.item = anvil.server.call('get_cart')
   
    if not self.item:
      self.empty_panel_1.visible = True
      self.column_panel_2.visible = False

    self.repeating_panel_1.items = self.item
   

  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("order_system")

  def outlined_button_2_click(self, **event_args):
    anvil.server.call('clear_items')
   
    
  

  

    


    