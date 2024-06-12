from ._anvil_designer import order_systemTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..view import view

class order_system(order_systemTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.view_items = []
    # Any code you write here will run before the form opens.

  def maincourse_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('order_system.maincourse')

  def stater_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('order_system.staters')

  def view_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form(view(items=self.view_items))
    
  def add_to_cart(self, product, quantity):
    #if item is already in cart, just update the quantity
     for i in self.view_items:
      if i['product'] == product:
        i['quantity'] += quantity
        break 
      else:
       self.view_items.append({'product': product, 'quantity': quantity})
 