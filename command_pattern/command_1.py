### Command pattern encapsulates a request (the command itself) can compose encapsulated commands into some process list
## and support undoable operations (able to undo a command)

from abc import ABC, abstractmethod

### ========
# Interfaces
### ========

class ICommand(object):
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        raise NotImplementedError("Execute method not yet implemented")

    def unexecute(self):
        raise NotImplementedError("Unexecute method not yet implemented")


class IReceiver(object):
    def on(self):
        raise NotImplementedError("On method not yet implemented")

    def off(self):
        raise NotImplementedError("Off method not yet implemented")

### =============
# Implementations
### =============

class Invoker(object):
    """ Onvoker objects. """

    def __init__(self, commands):
        self._commands = commands

    def add_command(self, command):
        """ Add command to commands list. """
        self._commands.append(command)

    def remove_command(self, command):
        """ Remove command from commands list. """
        self._commands.remove(command)

    def execute_commands(self):
        """ Execute all commands in commands list. """
        for command in self._commands:
            command.execute()

    def unexecute_commands(self):
        for command in reversed(self._commands):
            command.unexecute()

class OnCommand(ICommand):
    """ Command to turn on. """
    def execute(self):
        print('Executing ON command')

class OffCommand(ICommand):
    """ Command to turn off. """

    def execute(self):
        print('Executing OFF command')

class DimUpCommand(ICommand):
    """ Command to dim up. """

    def execute(self):
        print('Executing Dim Up command')

class DimDownCommand(ICommand):
    """ Command to dim down. """

    def execute(self):
        print('Executing Dim Down command')

class Receiver(IReceiver):
    """ Receiver object. """

    def action(self):
        print("Performing some action.")


def main():
    # Set up receiver
    receiver = Receiver()

    # Set up commands
    on_command = OnCommand(receiver)
    off_command = OffCommand(receiver)
    dim_up_command = DimUpCommand(receiver)
    dim_down_command = DimDownCommand(receiver)

    # Set up invoker
    invoker = Invoker([off_command, dim_up_command])

    # Test add commands
    invoker.add_command(on_command)
    invoker.add_command(dim_up_command)
    invoker.add_command(dim_down_command)
    invoker.add_command(dim_down_command)
    invoker.add_command(off_command)

    # Test remove commands
    invoker.remove_command(dim_down_command)

    # Execute invoker's commands
    invoker.execute_commands()

if __name__ == '__main__':
    main()