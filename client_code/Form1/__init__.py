from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form1(Form1Template):

  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
  def get_name_age(self, name, age):
    if name == "" or age == "":
      return "error"
    else:
      return f'My name is {name}. I am {age} years old.'

  def name_age_click(self, **event_args):
    self.output.text = self.get_name_age(self.name.text, self.age.text)
    
  def name_pressed_enter(self, **event_args):
    self.name_age_click()

  def age_pressed_enter(self, **event_args):
    self.name_age_click()




