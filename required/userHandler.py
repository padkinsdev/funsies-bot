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
    init_command = "CREATE TABLE users (snowflake_id INTEGER PRIMARY KEY, permissions VARCHAR(5), name VARCHAR(20))"
    crsr.execute(init_command)
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
  def retrieveUserPerms(self, userId):
    if self.userExists(userId):
      connection, crsr = self.connectToDB()
      crsr.execute("SELECT permissions FROM users WHERE snowflake_id = " + str(userId))
      return crsr.fetchone()
    else:
      return -1
  def userExists(self, userId):
    connection, crsr = self.connectToDB()
    crsr.execute("EXISTS " + str(userId))
    return crsr.fetchone()
