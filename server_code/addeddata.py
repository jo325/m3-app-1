import anvil.email
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


@anvil.server.callable
def add_item(name, description, price, image):
    # Add the new item to the Items table
    app_tables.menu_item.add_row(name=name, description=description, image=image,price=price)

