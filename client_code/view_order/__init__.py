from ._anvil_designer import view_orderTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class view_order(view_orderTemplate):
  def __init__(self,items, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    cart_items = anvil.server.call('get_cart_items')

        # Display the items
    for item in cart_items:
       self.empty_cart_panel.visible = True
       self.column_panel_1.visible = False
     self.repeating_panel_1.items = cart_items

    