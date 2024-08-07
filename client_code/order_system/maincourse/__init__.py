from ._anvil_designer import maincourseTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ...Product import Product
from .TableInfoForm import TableInfoForm

class maincourse(maincourseTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  
    products = anvil.server.call('get_products')
    for p in products:
      self.card_panel_2.add_component(Product(item=p))

  def placed_order_click(self, **event_args):
    """This method is called when the button is clicked"""
    dialog = TableInfoForm()
    alert(dialog, buttons=[])
