from ._anvil_designer import ItemTemplate2Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ...Product import Product
from .. import view_order

class ItemTemplate2(ItemTemplate2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.set_event_handler('x-getattr', self.item_event_handler)
    # Any code you write here will run before the form opens.
    self.view_order = view_order()
    self.column_panel_1.add_component(self.view_order)

  def delete_button_click(self, **event_args):
    get_open_form().view_order_items.remove(self.item)
    get_open_form().view_order_link_click()
    """This method is called when the button is clicked"""
    

  def item_event_handler(self, **event_args):
        self.label_name.text = self.item['name']
        self.image_1.source = self.item['imag']
        self.label_price.text = f"${self.item['price2']}"
        self.label_counter.text = str(self.item['counter_value'])
        self.total_num.text= f"${self.item['price2'] * self.item['counter_value']}"
 
  
  def add_card(self, item):
    """Add a card to the display"""
    card = Product()
    card.set_item(item)
    card.set_event_handler('x-add-to-cart', self.add_to_cart)
    self.card_panel.add_component(card)

  def add_to_cart(self, item, **event_args):
    """Add item to the cart in the view form"""
    self.view_order.add_to_cart(item)