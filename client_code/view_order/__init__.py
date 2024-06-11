from ._anvil_designer import view_orderTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Product import ProductTemplate

class view_order(view_orderTemplate):
  def __init__(self,items=None, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.repeating_panel_1.item_template=ProductTemplate
    if items:
            self.repeating_panel.items = items

  

  

    


    