from abc import ABC, abstractmethod

# Command interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# Simple commands
class LightOnCommand(Command):
    def execute(self):
        print("Light is ON")

class MusicPlayCommand(Command):
    def execute(self):
        print("Music is playing")

# Complex command assembled from simple commands
class ComplexCommand(Command):
    def __init__(self, commands):
        self.commands = commands

    def execute(self):
        for command in self.commands:
            command.execute()

# Client code
light_command = LightOnCommand()
music_command = MusicPlayCommand()

# Complex command assembling simple commands
complex_command = ComplexCommand([light_command, music_command])

# Execute complex command
complex_command.execute()
