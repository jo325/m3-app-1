from ._anvil_designer import ProductTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables



class Product(ProductTemplate):
  
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.item = None
    self.counter_value = 0
    self.counter_label.text = str(self.counter_value)

  def set_item(self, item):
    """Set the item details"""
    self.item = item
    self.label_name.text = item['name']
    self.label_price.text = f"${item['price2']}"
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
            'name': self.label_1,
            'image': self.image_1,
            'price': self.label_2,
            'counter': self.counter_value
        }
    self.raise_event('x-add-to-cart', item=item_data)
    anvil.server.call('save_temp_data', item_data)
        # Reset count after adding to cart
   
    self.counter_label.text = str(self.counter_value)
    
   
    
   