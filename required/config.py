import commandutils as cu
import permHandler as ph

class CommandStack:
  """
  Puts together the RequestQueue and CommandParser classes to make a clean command executor/permission checker
  """
  def __init__(self):
    self.gatekeeper = ph.RequestQueue()
    self.interpreter = cu.CommandParser()
    self.interpreter.setCommandLibPath("myCommands.py")
    self.interpreter.appendCommandsToList()
  def acceptCommand(self, commandName):
    command = self.interpreter.selectCommandByName(commandName)
    if command:
      self.gatekeeper.addNewRequest()
  def startFulfillEventLoop(self):
    pass

baseStack = CommandStack()
