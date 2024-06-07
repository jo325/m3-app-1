from ._anvil_designer import view_orderTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class view_order(view_orderTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.cart_items = anvil.server.call('get_cart_items') or []
  
    for items in self.cart_items:
        self.repeating_panel_1.items = self.cart_items

    


    