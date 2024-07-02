import anvil.email
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.users
from anvil.server import session, callable

@anvil.server.callable
def add_to_cart(table_no,date,time,name,price,quantity):
    # Check if the cart exists in the session, otherwise initialize it
    if 'cart' not in anvil.server.session:
        anvil.server.session['cart'] = []
    
    # Add the item to the cart
    anvil.server.session['cart'].append({"table_no":table_no,"date":date,"time":time,"name":name ,"price": price, "quantity": quantity})

@anvil.server.callable
def get_cart():
    # Retrieve the cart from the session
    cart = anvil.server.session.get('cart', [])
    return cart


@anvil.server.callable
def clear_items():
    """Clear all items from the session"""
    if 'cart' in session:
        del session['cart']


