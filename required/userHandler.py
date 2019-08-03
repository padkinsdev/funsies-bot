import json

class UserDatabase:
  def __init__(self):
    self.data = {}
  def parse_to_dict(self, fobj):
    """
    Extracts the data from a *raw* JSON file object into a Python dictionary
    """
    self.data = json.load(fobj)
    fobj.close()
  def get_field(self, field_name):
    if field_name in self.data.keys():
      return self.data[field_name]
    else:
      return None
  def write_field(self, field_name, value):
    if field_name in self.data.keys():
      self.data[field_name] = value
      return True
    else:
      return False
  def package_as_fobj(self, db_name="userDB.json"):
    with open(db_name, 'w') as datafile:
      json.dump(self.data, datafile)
      return datafile
