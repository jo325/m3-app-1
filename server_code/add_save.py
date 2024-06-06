
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


@anvil.server.callable
def add_to_cart(item_data):
  app_tables.cart_items.add_row(
      name1=item_data['name'],
      image1=item_data['image'],
      price3=item_data['price'],
      counter=item_data['counter']
  )

@anvil.server.callable
def get_cart_items():
    return app_tables.cart_items.search()