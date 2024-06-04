from ._anvil_designer import order_systTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Product import Product

class order_syst(order_systTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    products = app_tables.products.search()
    for p in products:
      self.flow_panel_1.add_component(Product(item=p), width='30%')





    # Any code you write here will run before the form opens.
