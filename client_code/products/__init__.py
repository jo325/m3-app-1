from ._anvil_designer import productsTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class products(productsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def increment_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def decrement_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass
