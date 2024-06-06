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
    self.order = []
    self.items = items

    if not self.items:
      self.empty_cart_panel.visible = True
      self.column_panel_1.visible = False
    
    self.repeating_panel_1.items = self.items
    

    # Any code you write here will run before the form opens.
