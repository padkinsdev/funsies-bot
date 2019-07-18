import sqlite3
from os.path import isfile
import pickle
from random import randint
from random import choices

class UserMarkov:
  """
  Updates itself using messages that a user sends, then is able to mimic the user's speech patterns
  """
  def __init__(self):
    self.probabilities = {}
    self.word_dists = {}
  def add_new_user(self, user_id):
    if user_id not in self.probabilities.keys():
      self.probabilities.update({user_id: {}})
      self.word_dists.update({user_id: {}})
  def update(self, message):
    readable = "<START> " + message.content + " <END>" 
    words = readable.split(" ")
    for i in range(1, len(words)-1):
      if words[i] != " ":
        if words[i] in self.probabilities[message.author.id].keys():
          self.probabilities[message.author.id][words[i]][words[i+1]] += 1
        else:
          self.probabilities[message.author.id].update({words[i]:{words[i+1]:1}})
  def calc_distributions(self, user_id):
    self.word_dists[user_id] = None
    for word in self.probabilities[user_id]:
      times_used = 0
      for next_word in self.probabilities[user_id][word]:
        times_used += self.probabilities[user_id][word][next_word]
      for next_word in self.probabilities[user_id][word]:
        self.word_dists[user_id].update({word: {next_word: float(self.probabilities[user_id][word][next_word])/float(times_used)}})
  def pickle_me(self):
    datacopy = [self.probabilities.copy(), self.word_dists.copy()]
    with open('markov_data.pkl', 'wb') as jar:
      pickle.dump(datacopy, jar)
  def unpickle_me(self):
    with open('markov_data.pkl', 'rb') as pkl_file:
      data = pickle.load(pkl_file)
      self.probabilities = data[0]
      self.word_dists = data[1]
  def gen_text(self, user_id):
    self.calc_distributions(user_id)
    final_text = ""
    text = ["<START>"]
    cur_word = "<START>"
    while cur_word != "<END>":
      words = []
      weighting = []
      for word in self.word_dists[user_id][cur_word].keys():
        words.append(word)
        weighting.append(self.word_dists[user_id][cur_word][word])
      new_word = choices(words, weights=weighting, cum_weights=1, k=1)
      text.append(new_word)
      cur_word = new_word
    for word in text:
      if word != "<START>" and word != "<END>":
        final_text += word + " "
    return final_text

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
    crsr.execute("DELETE FROM marriages WHERE user_one=" + str(user_two) + " AND user_two=" + str(user_one))
    connection.commit()
    connection.close()
  def get_marriages_for_user(self, user_id):
    connection, crsr = self.connectToDB()
    crsr.execute("SELECT user_one FROM marriages WHERE user_two = " + str(user_id))
    results = crsr.fetchone()
    crsr.execute("SELECT user_two FROM marriages WHERE user_one = " + str(user_id))
    final_results = []
    for item in results:
      final_results.append(item)
    results = crsr.fetchone()
    for item in results:
      final_results.append(item)
    return final_results
    

