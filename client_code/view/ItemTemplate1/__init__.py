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
    self.item = properties['item']
    self.name_s.text = self.item['name']
    self.price_label = f"${self.item['price']:.2f}"
    self.quantity_value.text = str(self.item['quantity'])
    # Any code you write here will run before the form opens.
