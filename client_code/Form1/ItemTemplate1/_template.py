from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class ItemTemplate1Template(DataRowPanel):

  def init_components(self, **properties):
  	# Initialise GridPanel
    super().__init__()

    # Initialise custom properties here
    self.item = properties.get('item', {})
