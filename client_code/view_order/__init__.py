from ._anvil_designer import view_orderTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Product import ProductTemplate

class view_order(view_orderTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    def refresh_items(self):
        """Refresh the displayed items"""
        items = anvil.server.call('get_items')
        self.retevie_panel_1.clear()  # Assuming you have a FlowPanel named flow_panel_1
        for item in items:
            self.add_item_to_flow_panel(item)
    
    def add_item_to_flow_panel(self, item):
        """Add a single item to the FlowPanel"""
        item_label = Label(text=f"Name: {item['name']}, Price: {item['price']}, Quantity: {item['quantity']}")
        self.info =item_label
        self.retevie_panel_1.add_component(item_label)
    
   
      
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('view_product')

  

  

    


    