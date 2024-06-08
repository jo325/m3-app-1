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
    self.cart_items = []
    

  def add_to_cart(self, item):
    """Add item to cart and display"""
    self.cart_items.append(item)
    self.refresh_cart()

  def refresh_cart(self):
    """Refresh the cart display"""
    self.repeating_panel_cart.items = self.cart_items

  def form_show(self, **event_args):
    """This method is called when the form is shown on the screen"""
    self.refresh_cart()

    


    