import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ._anvil_designer import AdminFormTemplate
from anvil import *


class AdminForm(AdminFormTemplate):

    def __init__(self, item=None, **properties):
        self.init_components(**properties)
        self.item = item
        
        if self.item:
            self.name_textbox.text = self.item['name']
            self.description_textbox.text = self.item['description']
            self.price_numberbox.number = self.item['price']
            self.image_fileloader.visible = False  # Hide the file loader when editing
        
    def save_button_click(self, **event_args):
        name = self.name_textbox.text
        description = self.description_textbox.text
        price = self.price_numberbox.number
        image = self.image_fileloader.file
        
        if not name or not description or price is None:
            alert("All fields are required!")
            return
        
        if self.item:
            # Update existing item
            self.item.update(name=name, description=description, price=price)
            if image:
                self.item.update(image=image)
        else:
            # Add new item
            anvil.server.call('add_item', name, description, price, image)
        
        open_form('AdminDashboard')
    
    def cancel_button_click(self, **event_args):
        open_form('AdminDashboard')

