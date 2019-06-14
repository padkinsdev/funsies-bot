from config import CommandStack

class RequestQueue:
  """
  A RequestQueue object MUST BE created in order for the decorators to be usable
  """
  def __init__(self):
    self.__queue = {}
    self.__currentRequestId = 0
  
  def addNewRequest(self, requestId, serverId, userId, content):
    self.__queue.update({int(requestId): RequestDetails(serverId, userId, content)})
  
  def fetchRequest(self, requestId):
    if (requestId not in self.__queue.keys()):
      return None
    else:
      return self.__queue[requestId]
  
  def getNextId(self):
    """
    Returns the id number that should be assigned to the next command execution request that is appended to self.__queue
    """
    return max(self.__queue.keys()) + 1
  
  def getQueue(self, callerObj):
    """
    Should restrict view access of the request queue to only the CommandStack object that is handling all commands.
    """
    if isinstance(callerObj, CommandStack):
      return self.__queue
    else:
      return None
  
  def popRequest(self, requestId):
    self.__queue.pop(requestId)

  def fulfillNextRequest(self):
    self.__currentRequestId = min(self.__queue.keys())
    command = self.__queue.pop(self.__currentRequestId, None)
    return command
  
  def requiresPermission(self, permissionList):
    """
    Checks to see if the user in question has permission to call the command, and, if so, continues with the command execution. Otherwise returns None
    """
    def decorator(func):
      def decorated(*args, **kwargs):
        request = self.fetchRequest(self.__currentRequestId)
        userPerms = self._getUserPerms(request.userId)
        canCall = True
        for permission in permissionList:
          if permission not in userPerms:
            canCall = False
        if (canCall):
          return func(*args, *kwargs)
        return False #else
      return decorated
    return decorator

  def serverSpecific(self, serverIds):
    """
    Checks to see if the command is specific to a particular server (in other words, shouldn't be callable from other servers), and reacts accordingly
    """
    def decorator(func):
      def decorated(*args, **kwargs):
        request = self.fetchRequest(self.__currentRequestId)
        thisId = request.serverId
        if (thisId in serverIds):
          return func(*args, **kwargs)
        return False #else
      return decorated
    return decorator

  def _getUserPerms(userId):
    pass
    # NEEDS TO BE DEVELOPED

class RequestDetails:
  def __init__(self, serverId, userId, content):
    """
    Vanilla object representing the details of a request 

    Args: The id of the user that requested to use the command, and the id of the server from which the request came
    """
    self.serverId = serverId
    self.userId = userId
    self.content = content
