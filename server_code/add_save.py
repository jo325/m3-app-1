
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def add_menu_item(name, description, price, image):
    app_tables.add_menu_item.add_row(
        nametag=name,
        description=description,
        price=price,
        image=image
    )


