from ._anvil_designer import ItemTemplate1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class ItemTemplate1(ItemTemplate1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def form_refreshing_data_bindings(self, **event_args):
    """This method is called when refresh_data_bindings is called"""
    self.name.text=self.item['name']
    self.price_l.text=self.item['price']
    self.quantity_l.text=self.item['counter']
    self.total_cost.text=self.price_l*self.price_l
    self.repeating_panel_1.items = get_open_form().cart_items
