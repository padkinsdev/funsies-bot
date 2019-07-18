import sqlite3
from os.path import isfile

class UserDatabase:
  def __init__(self):
    self.__path = "userDB.db"
    if isfile(self.__path):
      pass
    else:
      self.createDataBase()
  def createDataBase(self):
    connection, crsr = self.connectToDB()
    init_one = "CREATE TABLE users (snowflake_id INTEGER PRIMARY KEY, permissions VARCHAR(5), name VARCHAR(20))"
    crsr.execute(init_one)
    init_two = "CREATE TABLE marriages (marriage_id INTEGER PRIMARY KEY, user_one INTEGER, user_two INTEGER)"
    crsr.execute(init_two)
    connection.commit()
    connection.close()
  def connectToDB(self):
    connection = sqlite3.connect(self.__path)
    crsr = connection.cursor()
    return connection, crsr
  def insertNewUser(self, userId, permissionInt, username):
    connection, crsr = self.connectToDB()
    crsr.execute("INSERT INTO users VALUES (" + str(userId) + ", \"" + str(permissionInt) + "\", \"" + str(username) + "\");")
    connection.commit()
    connection.close()
  def modifyEntry(self, userId, newPermissions=None, newUsername=None):
    connection, crsr = self.connectToDB()
    if newPermissions:
      crsr.execute("UPDATE users SET permissions = \"" + str(newPermissions) + "\" WHERE snowflake_id = " + str(userId))
    if newUsername:
      crsr.execute("UPDATE users SET name = \"" + str(newUsername) + "\" WHERE snowflake_id = " + str(userId))
    connection.commit()
    connection.close()
  def retrieveUserPerms(self, userId, username):
    connection, crsr = self.connectToDB()
    crsr.execute("SELECT permissions FROM users WHERE snowflake_id = " + str(userId))
    result = crsr.fetchone()
    if result:
      return result[0]
    else:
      self.insertNewUser(str(userId), "1", str(username))
      return "1"
  #def userExists(self, userId):
  #  connection, crsr = self.connectToDB()
  #  crsr.execute("EXISTS " + str(userId))
  #  return crsr.fetchone()
  def new_marriage(self, user_one, user_two):
    connection, crsr = self.connectToDB()
    crsr.execute("SELECT COUNT(marriage_id) FROM marriages")
    last_id = int(crsr.fetchone()[0])
    crsr.execute("INSERT INTO marriages VALUES (" + str(last_id+1) + ", " + str(user_one) + ", " + str(user_two) + ")")
    connection.commit()
    connection.close()
  def delete_marriage(self, user_one, user_two):
    connection, crsr = self.connectToDB()
    crsr.execute("DELETE FROM marriages WHERE user_one=" + str(user_one) + " AND user_two=" + str(user_two))
    connection.commit()
    connection.close()
  def get_marriages_for_user(self, user_id):
    connection, crsr = self.connectToDB()
    crsr.execute("SELECT user_one FROM marriages WHERE user_two = " + str(user_id))
    results = crsr.fetchone()
    crsr.execute("SELECT user_two FROM marriages WHERE user_one = " + str(user_id))
    results += crsr.fetchone()
    return results
    

