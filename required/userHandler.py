import required.modify_db as modb

class UserDatabase:
  def __init__(self):
    self.fname = "userDB.db"
    self.fields = ["user_id INTEGER PRIMARY KEY", "afk TEXT", "level INTEGER", "balance INTEGER", "activity INTEGER"]
    self.server_fields = ["server_id INTEGER PRIMARY KEY", "gif_url TEXT"]
  def create_anew(self):
    modb.initialize("/tmp/" + self.fname)
  def get_field(self, user_id, field_name):
    value = modb.get_field(self.fname, user_id, field_name)
    if value is None:
      if not modb.check_table_exists(self.fpath, str(user_id)[:13]+"_data"):
        modb.create_table(self.fpath, str(user_id)[:13]+"_data", "(" + " ".join(self.fields) + ")")
      self.add_new_user(user_id)
      return None
    else:
      return value
  def write_field(self, user_id, field_name, value):
    success = modb.write_field(self.fpath, user_id, field_name, value)
    if not success:
      if not modb.check_table_exists(self.fpath, str(user_id)[:13]+"_data"):
        modb.create_table(self.fpath, str(user_id)[:13]+"_data", "(" + " ".join(self.fields) + ")")
      self.add_new_user(user_id)
      modb.write_field(self.fpath, user_id, field_name, value)
      return False
    else:
      return True
  def add_to_field(self, user_id, field_name, add_amount):
    try:
      value = self.get_field(user_id, field_name)
      if value:
        endval = int(value) + int(add_amount)
      else:
        endval = add_amount
      self.write_field(user_id, field_name, endval)
    except Exception as err:
      print(err)
  def add_new_user(self, user_id, values=None):
    if len(values.split(",")) != len(self.fields):
      values = None
    if values is None:
      values = "("
      for i in range(0, len(self.fields)):
        values = values + "0"
        if i < len(self.fields)-1:
          values = values + ", "
    modb.add_new_user(self.fpath, user_id, values)
  def delete_field(self, user_id, field_name):
    modb.write_field(self.fpath, user_id, field_name, "0")
