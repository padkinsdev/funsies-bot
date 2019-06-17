class PermissionInteger:
  def __init__(self):
    self.permlist = {"not_muted": 1, "no_cooldown": 2, "trusted": 4, "premium": 8}
  def getPermInteger(self, permList):
    finalInt = 0
    for permission in permList:
      if permission in self.permlist.keys():
        finalInt += self.permlist[permission]
    return finalInt
