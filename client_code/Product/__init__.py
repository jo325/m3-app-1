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
  
    self.counter_value = 0
    self.counter_label.text = str(self.counter_value)
    self.temp_storage = [] 
  
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
    name = self.name2.text
    price = self.price2.text
    quantity = self.counter_value.numerator
    
    # Store the item data in the temp_storage variable
    self.temp_storage.append({"name": name, "price": price, "quantity": quantity})
    Notification("data is saved")
    open_form('view', temp_storage=self.temp_storage)
 
