import required.userHandler as userHandler
import required.permissions as permissions
import required.aws_bucket as aws_bucket
import os
#import botfiles.bot_data as bot_data

class Commandler:
  def __init__(self):
    self.userDB = userHandler.UserDatabase()
    self.perms = permissions.PermissionInteger()
    self.bucket_handler = aws_bucket.AWSBucketManager(os.environ["AWS_BUCKET_NAME"])
  def requiresPermission(self, permList):
    def decorator(func):
      def decorated(message):
        userPerms = int(self.userDB.get_field("permissions"))
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
  def get_db(self, db_name="userDB.json"):
    db_fobj = self.bucket_handler.get_as_file(db_name)
    self.userDB.parse_to_dict(db_fobj)
  def upload_db(self, db_name="userDB.json"):
    db_fobj = self.userDB.package_as_fobj(db_name=db_name)
    self.bucket_handler.upload_file(db_fobj, db_name)
