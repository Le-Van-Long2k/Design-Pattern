# *********************************************************************
# Command interface
from abc import ABC, abstractmethod


class Command(ABC):

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


# *********************************************************************
# Receiver
class Device:
    def turnOn(self):
        print("Device ON")

    def turnOff(self):
        print("Device OFF")


# *********************************************************************
# Concrete command
class TurnOnCommand(Command):
    def __init__(self, device: Device):
        self.device = device

    def execute(self):
        self.device.turnOn()

    def undo(self):
        self.device.turnOff()


class TurnOffCommand(Command):
    def __init__(self, device: Device):
        self.device = device

    def execute(self):
        self.device.turnOff()

    def undo(self):
        self.device.turnOn()


# *********************************************************************
# Invoker
class RemoteControl:
    def __init__(self):
        self._undo_stack = []

    def setCommand(self, command: Command):
        self.command = command

    def executeCommand(self):
        self.command.execute()
        self._undo_stack.append(self.command)

    def undo(self):
        pre_command: Command = self._undo_stack.pop()
        pre_command.undo()


tv = Device()

turnOnCommand = TurnOnCommand(tv)
turnOffCommand = TurnOffCommand(tv)
remote = RemoteControl()

remote.setCommand(turnOnCommand)
remote.executeCommand()
remote.undo()

remote.setCommand(turnOnCommand)
remote.executeCommand()

remote.setCommand(turnOffCommand)
remote.executeCommand()

remote.setCommand(turnOffCommand)
remote.executeCommand()


remote.undo()
remote.undo()
remote.undo()
