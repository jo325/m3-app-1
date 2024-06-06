from ._anvil_designer import view_orderTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from..Product import cart_items

class view_order(view_orderTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

   
   
        # Display the items
    if not cart_items:
       self.empty_panel_1.visible = True
       self.column_panel_2.visible = False

    self.repeating_panel_1.items = cart_items


    