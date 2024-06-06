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
      get_open_form().Product(self.item, self.counter_label.text)
      self.counter_label.text = ""
      self.add_button.visible = True
      self.timer_1.interval = 1
     else:
        self.counter_label.text = ""
        Notification("Please specify a quantity").show()


  def timer_1_tick(self, **event_args):
    """This method is called Every [interval] seconds. Does not trigger if [interval] is 0."""
    self.add_button.visible = True
    self.added_button.visible = False
    self.timer_1.interval = 0
    
  
    
   