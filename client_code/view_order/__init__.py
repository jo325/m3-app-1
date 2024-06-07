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
    
    self.load_temp_data()

  def load_temp_data(self):
    temp_products = anvil.server.call('get_temp_data')
    
    self.repeating_panel_1.items = temp_products
        

    


    