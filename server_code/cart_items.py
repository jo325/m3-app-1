import anvil.email
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.users
from anvil.server import session, callable

@anvil.server.callable
def add_to_cart(name,price,quantity):
    # Check if the cart exists in the session, otherwise initialize it
    if 'cart' not in anvil.server.session:
        anvil.server.session['cart'] = []
    
    # Add the item to the cart
    anvil.server.session['cart'].append({"name":name ,"price": price, "quantity": quantity})

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


@anvil.server.callable
def add_to_cart_1(table_no,date,time):
    # Check if the cart exists in the session, otherwise initialize it
   name = anvil.server.session.get('cart', ["name"])
   quantity = anvil.server.session.get('cart', ["quantity"]) 
   price = anvil.server.session.get('cart', ["price"])
   if 'card' not in anvil.server.session:
        anvil.server.session['card'] = []
    
    # Add the item to the cart
   anvil.server.session['card'].append({"table_no":table_no,"date":date,"time":time,"name":name ,"price": price, "quantity": quantity})

@anvil.server.callable
def get_cart_1():
    # Retrieve the cart from the session
    card = anvil.server.session.get('card', [])
    return card
