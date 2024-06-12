from ._anvil_designer import view_productTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Product import Product

class view_product(view_productTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.current_index = 0 
   
    # Any code you write here will run before the form opens.

  def form_refreshing_data_bindings(self, **event_args):
    """This method is called when refresh_data_bindings is called"""
    item = anvil.server.call('get_item', self.current_index)
    if item:
            self.name.text = item['name']
            self.price_label.text = item['price']
            self.quantity_label.text = item['quantity']
            self.current_index += 1
    else:
            alert('No more items.')
            self.current_index = 0