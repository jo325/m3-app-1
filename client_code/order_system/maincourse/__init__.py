from ._anvil_designer import maincourseTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Product import Product

class maincourse(maincourseTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    products = anvil.server.call('get_products')
    for p in products:
      self.card_panel.add_component(Product(item=p), width='40%')
    # Any code you write here will run before the form opens.
