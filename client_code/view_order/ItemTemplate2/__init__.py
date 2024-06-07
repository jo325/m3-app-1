from ._anvil_designer import ItemTemplate2Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class ItemTemplate2(ItemTemplate2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def delete_button_click(self, **event_args):
    get_open_form().view_order_items.remove(self.item)
    get_open_form().view_order_link_click()
    """This method is called when the button is clicked"""
    

  def set_data_bindings(self, **event_args):
        self.label_name.text = self.item['product']['name']
        self.image_1.source = self.item['product']['imag']
        self.label_price.text = self.item['product']['price2']
        self.label_counter.text = str(self.item['counter_value'])