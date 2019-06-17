import userHandler
import permissions

class Commandler:
  def __init__(self):
    self.userDB = userHandler.UserDatabase()
    self.perms = permissions.PermissionInteger()
  def requiresPermission(self, permList):
    def decorator(func):
      def decorated(message):
        userPerms = self.userDB.retrieveUserPerms(message.author.id)
        if userPerms < 0:
          self.userDB.insertNewUser(message.author.id, 1, str(message.author.name))
        truePerms = self.perms.getPermInteger(permList)
        if (userPerms & truePerms) == truePerms:
          return func(message)
        else:
          return None
      return decorated
    return decorator
  def serverSpecific(self, enabledServers):
    def decorator(func):
      def decorated(message):
        if message.guild.id in enabledServers:
          return func(message)
        else:
          return None
      return decorated
    return decorator
