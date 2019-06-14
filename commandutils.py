import os
import sys
import importlib

class Command:
  def __init__(self, function, name="Unnamed", description="No description"):
    self.name = name
    self.description = description
    self.__func = function
  def __call__(self, *args, **kwargs):
    self.__func(*args, **kwargs)

class CommandParser:
  def __init__(self):
    self.commandList = {}
  def selectCommandByName(self, name):
    if name in self.commandList.keys():
      return self.commandList[name]
    else:
      return None
  def setCommandLibPath(self, filePath):
    os.environ['CMD_LIB'] = filePath
  def liftCommands(self):
    """
    Generator function that returns the bot commands in a python file
    """
    path = os.environ.get("CMD_LIB")
    modNameComponents = path.split("/")
    modName = modNameComponents[len(modNameComponents)-1]
    importlib.import_module(modName, __name__)
    for item in sys.modules[modName]:
      if callable(item):
        yield Command(item, name=item.__name__)
  def appendCommandsToList(self):
    """
    Uses self.listCommands to create a list of usable commands
    """
    for command in self.liftCommands():
      self.commandList.update({command.name: command})
