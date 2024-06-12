
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from anvil.server import session, callable

@anvil.server.callable
def add_menu_item(name, description, price, image):
    app_tables.add_menu_item.add_row(
        nametag=name,
        description=description,
        price=price,
        image=image
    )


@anvil.server.callable
def get_products():
  return app_tables.product.search()

@callable
def set_item(name0, price01, counter23):
    """Set an item in the session"""
    if 'items' not in session:
        session['items'] = []
    session['items'].append({
        'name': name0,
        'price': price01,
        'quantity': counter23
    })

@callable
def get_items():
    """Get all items from the session"""
    return session.get('items', [])

@callable
def get_item(index):
    """Get a single item from the session by index"""
    items = session.get('items', [])
    if index < len(items):
        return items[index]
    else:
        return None

@callable
def remove_first_item():
    """Remove the first item from the session"""
    if 'items' in session and session['items']:
        session['items'].pop(0)