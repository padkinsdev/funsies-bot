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
    if user_id in self.data.keys():
      if field_name in self.data[user_id].keys():
        return self.data[user_id][field_name]
      else:
        return None
    else:
      self.add_new_user(user_id)
      return None
  def write_field(self, user_id, field_name, value):
    if user_id in self.data.keys():
      if field_name in self.data[user_id].keys():
        self.data[user_id][field_name] = value
        return True
      else:
        self.data[user_id].update({field_name: value})
    else:
      self.data.update({user_id: {field_name: value}})
    return False
  def package_as_fobj(self, db_name="userDB.json"):
    with open(db_name, 'w') as dfile:
      json.dump(self.data, dfile)
    datafile = open(db_name, 'rb')
    return datafile
  def add_new_user(self, user_id, field_dict={}):
    if user_id not in self.data.keys():
      self.data.update({user_id: field_dict})
