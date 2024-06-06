from ._anvil_designer import order_systemTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class order_system(order_systemTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def maincourse_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('order_system.maincourse')

  def stater_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('order_system.staters')

  def view_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('view_order')
    
