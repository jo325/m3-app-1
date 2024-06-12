from ._anvil_designer import ProductTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..view import view
from ..order_system import order_system


class Product(ProductTemplate):
  
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
  
    self.counter_value = 0
    self.counter_label.text = str(self.counter_value)
   
  
    # Any code you write here will run before the form opens.

  def increment_button_click(self, **event_args):
    self.counter_value += 1
    self.counter_label.text = str(self.counter_value)
    # Save the new counter value to the database

  
  def decrement_button_click(self, **event_args):
    self.counter_value -= 1
    self.counter_label.text = str(self.counter_value)
    # Save the new counter value to the database

  def add_button_click(self, **event_args):
   if self.counter_label.text:
      getform=order_system()
      getform.add_to_cart(self.item,quantity=self.counter_value)
      self.counter_label.text = ""
      
   else:
        self.counter_label.text = ""
        Notification("Please specify a quantity").show()

  
 
 
