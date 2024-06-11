from ._anvil_designer import ProductTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..view_order import view_order


class Product(ProductTemplate):
  
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.items = []
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
   name0 = self.name2
   price01 = self.price2.text
   counter23 = int(self.counter_value)
    
   card_data = {
            'name': name0,
            'price': price01,
            'counter': counter23
        }
   self.items.append(card_data)

  def add_button_show(self, **event_args):
   display_form=view_order(items=self.items)
   get_open_form().column_panel_1.add_component(display_form)
   

 
