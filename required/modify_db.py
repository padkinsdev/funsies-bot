import sqlite3 as sl
# I know that I should be using decorators :/

def initialize(fpath):
  """
  THIS WILL CRUDELY WIPE OUT ANY DATA IN THE FILE AT fpath, SO USE IT CAREFULLY
  """
  with open(fpath, 'w') as init:
    pass
  conn = sl.connect(fpath)
  crsr = conn.cursor()
  crsr.execute('CREATE TABLE id_ranges (beginning_digits INTEGER PRIMARY KEY, table_name VARCHAR(25));')
  crsr.execute('INSERT INTO id_ranges VALUES (0, 0);')
  conn.commit()
  conn.close()
  # On the previous line, a table was created in the database which maps snowflake id number ranges to names of tables that contain the data on users with ids in those ranges

def wipe_table(fpath, table_name):
  """
  Essentially implements the DROP TABLE sql method. Should also be used carefully
  """
  conn = sl.connect(fpath)
  crsr = conn.cursor()
  crsr.execute("DROP TABLE {}".format(table_name))
  conn.commit()
  conn.close()

def create_table(fpath, table_name, fields):
  # fields would be a string that looks something like "(user_id INTEGER, perm_int INTEGER)"
  conn = sl.connect(fpath)
  crsr = conn.cursor()
  crsr.execute("CREATE TABLE {} {}".format(table_name, fields))
  crsr.execute("INSERT INTO id_ranges VALUES {} {}".format(table_name[:13], str(table_name)+"_data"))
  conn.commit()
  conn.close()

def get_field(fpath, user_id, field_name):
  conn = sl.connect(fpath)
  crsr = conn.cursor()
  if check_user_exists(fpath, user_id):
    crsr.execute("SELECT " + str(field_name) + " FROM " + str(user_id)[:13] + "_data WHERE user_id = '" + str(user_id) + "';")
    final_val = crsr.fetchone()[0]
    conn.commit()
    conn.close()
    return final_val
  else:
    conn.close()
    return None

def check_table_exists(fpath, table_name):
  conn = sl.connect(fpath)
  crsr = conn.cursor()
  crsr.execute("SELECT COUNT(table_name) FROM id_ranges WHERE beginning_digits = '" + table_name + "';")
  result = crsr.fetchone()[0]
  conn.close()
  if result == 1:
    return True
  else:
    return False

def check_user_exists(fpath, user_id):
  conn = sl.connect(fpath)
  crsr = conn.cursor()
  if check_table_exists(fpath, str(user_id)[:13] + "_data"):
    crsr.execute("SELECT COUNT(user_id) FROM " + str(user_id)[:13] + "_data WHERE user_id = '" + str(user_id) + "';")
    result = crsr.fetchone()[0]
    conn.close()
    if result == 1:
      return True
    else:
      return False
  else:
    conn.close()
    return False

def write_field(fpath, user_id, field_name, value):
  conn = sl.connect(fpath)
  crsr = conn.cursor()
  if check_user_exists(fpath, user_id):
    crsr.execute("UPDATE " + str(user_id)[:13] + "_data SET " + str(field_name) + " = " + str(value) + " WHERE user_id = " + str(user_id))
    conn.commit()
    conn.close()
    return True
  else:
    conn.close()
    return False

def add_new_user(fpath, user_id, values):
  """
  values should be a string (...,...,...)
  """
  if not check_table_exists(fpath, str(user_id)[:13]):
    return False
  else:
    conn = sl.connect(fpath)
    crsr = conn.cursor()
    crsr.execute("INSERT INTO " + str(user_id)[:13] + "_data VALUES " + values)
    conn.commit()
    conn.close()
    return True

def add_new_server(fpath, server_id):
  conn = sl.connect(fpath)
  crsr = conn.cursor()
  crsr.execute("INSERT INTO servers (server_id) VALUES (" + str(server_id) + ");")
  conn.commit()
  conn.close()

def change_server_settings(fpath, server_id, field_name, value):
  conn = sl.connect(fpath)
  crsr = conn.cursor()
  crsr.execute("UPDATE servers SET " + str(field_name) + " = " + str(value) + " WHERE server_id = " + str(server_id))
  conn.commit()
  conn.close()
