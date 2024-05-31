from ._anvil_designer import temp1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class temp1(temp1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def save_box_click(self, **event_args):
     name = self.nametag_box.text
     description = self.description_box.text
     price = self.price_box.text
     image = self.image_fileloader.file
     
     if not name or not description or price is None or not image:
      alert("All fields are required!")
      return

        # Call the server function to add the item to the database
      anvil.server.call('add_item', name, description, price, image)
      alert("Item saved successfully!")
        # Optionally clear the form after saving
      self.name_textbox.text = ""
      self.description_textbox.text = ""
      self.price_numberbox.text = None
      self.image_fileloader.clear()

 
    
