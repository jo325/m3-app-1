from ._anvil_designer import order_systemTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..view import view

class order_system(order_systemTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.
    self.cart_items = self.get_cart_items()

  def get_cart_items(self):
        # Fetch the cart items from the server
        return anvil.server.call('get_cart')

  def build_cart(self):
       
        self.cart_grid (
            columns=[
                {"title": "Item", "key": "name"},
                {"title": "Price", "key": "price"},
                {"title": "Quantity", "key": "quantity"}
            ],
            rows=self.cart_items
        )
        self.cart_panel.add_component(self.cart_grid)
        return self.cart_panel
   
  def maincourse_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('order_system.maincourse')

  def stater_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('order_system.staters')

  def view_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("view")

  
    
  