import sqlite3
from os.path import isfile
import required.aws_bucket

class UserDatabase:
  def __init__(self):
    self.__path = "userDB.db"
    if isfile(self.__path):
      pass
    else:
      self.createDataBase()
  def createDataBase(self):
    connection, crsr = self.connectToDB()
    init_one = "CREATE TABLE users (snowflake_id INTEGER PRIMARY KEY, permissions VARCHAR(5), balance INTEGER)"
    crsr.execute(init_one)
    connection.commit()
    connection.close()
  def connectToDB(self):
    connection = sqlite3.connect(self.__path)
    crsr = connection.cursor()
    return connection, crsr
  def insertNewUser(self, userId, permissionInt):
    connection, crsr = self.connectToDB()
    crsr.execute("INSERT INTO users VALUES (" + str(userId) + ", \"" + str(permissionInt) + "\", \"0\");")
    connection.commit()
    connection.close()
  def modifyEntry(self, userId, newPermissions=None, newBal=None):
    connection, crsr = self.connectToDB()
    if newPermissions:
      crsr.execute("UPDATE users SET permissions = \"" + str(newPermissions) + "\" WHERE snowflake_id = " + str(userId))
    if newBal:
      crsr.execute("UPDATE users SET balance = \"" + str(newBal) + "\" WHERE snowflake_id = " + str(userId))
    connection.commit()
    connection.close()
  def retrieveUserPerms(self, userId):
    connection, crsr = self.connectToDB()
    crsr.execute("SELECT permissions FROM users WHERE snowflake_id = " + str(userId))
    result = crsr.fetchone()
    if result:
      return result[0]
    else:
      self.insertNewUser(str(userId), "1")
      return "1"
  def retrieveUserBal(self, userId):
    connection, crsr = self.connectToDB()
    crsr.execute("SELECT balance FROM users WHERE snowflake_id = " + str(userId))
    result = crsr.fetchone()
    if result:
      return result[0]
    else:
      self.insertNewUser(str(userId), "0")
      return "0"
  def add_to_bal(self, user_id, amount):
    balance = int(self.retrieveUserBal(user_id))
    balance += amount
    self.modifyEntry(user_id, newBal=balance)
