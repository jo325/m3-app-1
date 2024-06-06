from ._anvil_designer import ProductTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
cart_items = []

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
    item_data = {
            'name': self.item['name'],
            'image': self.item['imag'],
            'price': self.item['price2'],
            'counter': self.counter_value
        }
    
    cart_items.append(item_data)
        # Reset count after adding to cart
    self.count = 0
    self.counter_label.text = str(self.count)
    
    
  
    
   