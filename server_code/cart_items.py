import anvil.email
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.users


@anvil.server.callable
def add_to_cart(item):
    # Check if the cart exists in the session, otherwise initialize it
    if 'cart' not in anvil.server.session:
        anvil.server.session['cart'] = []
    
    # Add the item to the cart
    anvil.server.session['cart'].append(item)

@anvil.server.callable
def get_cart():
    # Retrieve the cart from the session
    cart = anvil.server.session.get('cart', [])
    return cart