from ._anvil_designer import order_systTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Product import Product

class order_syst(order_systTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    products = app_tables.product.search()
    for p in products:
      self.flow_panel_1.add_component(Product(item=p), width='40%')





    # Any code you write here will run before the form opens.

  def main_course_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('order_syst.main_course1')

  def reset_links(self, **event_args):
   self.contact_us_link.role = ''
   self.about_us_link.role = ''

  def staters_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('order_syst.staters_v')
