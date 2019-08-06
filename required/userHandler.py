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
    print(self.data)
  def get_field(self, user_id, field_name):
    if str(user_id) in self.data.keys():
      if str(field_name) in self.data[str(user_id)].keys():
        return self.data[str(user_id)][str(field_name)]
      else:
        return None
    else:
      self.add_new_user(user_id)
      return None
  def write_field(self, user_id, field_name, value):
    if str(user_id) in self.data.keys():
      if str(field_name) in self.data[user_id].keys():
        self.data[str(user_id)][str(field_name)] = str(value)
        return True
      else:
        self.data[user_id].update({str(field_name): str(value)})
    else:
      self.data.update({str(user_id): {str(field_name): str(value)}})
    return False
  def package_as_fobj(self, db_name="userDB.json"):
    with open(db_name, 'w') as dfile:
      json.dump(self.data, dfile)
    datafile = open(db_name, 'rb')
    return datafile
  def add_new_user(self, user_id, field_dict={}):
    if str(user_id) not in self.data.keys():
      self.data.update({str(user_id): field_dict})
