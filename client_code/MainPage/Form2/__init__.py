from ._anvil_designer import Form2Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Form2(Form2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def save_box_click(self, **event_args):
        name = self.name_box.text
        description = self.description_textarea.text
        price_str = self.price_box.text
        image = self.image_fileloader.file

        # Convert price to a number
        try:
            price = float(price_str)
        except ValueError:
            alert("Please enter a valid number for the price.")
            return

        # Call the server function to add the menu item
        anvil.server.call('add_menu_item', name, description, price, image)
    
        alert("Menu item added successfully!")
        # Clear the form fields
        self.name_textbox.text = ""
        self.description_textarea.text = ""
        self.price_textbox.text = ""
        self.image_fileloader.clear()
    
