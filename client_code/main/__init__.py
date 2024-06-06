from ._anvil_designer import mainTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class main(mainTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def view_cart_click(self, **event_args):
    open_form('view_order')
  

  def order_now_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('order_system')

  def update_panel_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('main.Form2')
    
