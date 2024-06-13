import anvil.email
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.users
cart = []

@anvil.server.callable
def add_to_cart(item):
    cart.append(item)

@anvil.server.callable
def get_cart_items():
    return cart