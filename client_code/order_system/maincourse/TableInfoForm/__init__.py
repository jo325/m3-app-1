from ._anvil_designer import TableInfoFormTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class TableInfoForm(TableInfoFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    
    """This method is called when the button is clicked"""
    table_no = self.table_no.text
    date = self.date_picker_1.date
    time = self.time_no.text

        # Return the values and close the dialog
    
    anvil.server.call('add_to_cart_1',table_no, date ,time)
    open_form('order_system.maincourse')
   
    
