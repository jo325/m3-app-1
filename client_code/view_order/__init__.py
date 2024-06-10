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
    

  def add_to_cart(self, card_data):
        self.cart_items.append(card_data)
        self.update_cart_view()

  def update_cart_view(self):
        self.view_cart_repeating_panel.items = self.cart_items

    


    