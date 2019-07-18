import required.userHandler as userHandler
import required.permissions as permissions

class Commandler:
  def __init__(self):
    self.userDB = userHandler.UserDatabase()
    self.perms = permissions.PermissionInteger()
    self.markovian = userHandler.UserMarkov()
  def requiresPermission(self, permList):
    def decorator(func):
      def decorated(message):
        userPerms = int(self.userDB.retrieveUserPerms(message.author.id, message.author.name))
        #if userPerms < 0:
        #  self.userDB.insertNewUser(message.author.id, 1, str(message.author.name))
        #  userPerms = 1
        truePerms = self.perms.getPermInteger(permList)
        if (userPerms & truePerms) == truePerms:
          return func(message)
        else:
          print("Failed permissions check")
          return None
      return decorated
    return decorator
  def serverSpecific(self, enabledServers):
    def decorator(func):
      def decorated(message):
        if message.guild.id in enabledServers:
          return func(message)
        else:
          print("Failed server specific check")
          return None
      return decorated
    return decorator
