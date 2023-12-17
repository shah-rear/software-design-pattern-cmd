from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class DeferredCommand(Command):
    def __init__(self, receiver, action):
        self.receiver, self.action = receiver, action

    def execute(self):
        print(f"Ertelemeli İşlem: {self.action}")
        self.receiver.perform_action()

class Receiver:
    def perform_action(self):
        print("İşlem Gerçekleştirildi")

class Invoker:
    def __init__(self, deferred_commands=[]):
        self.deferred_commands = deferred_commands

    def add_deferred_command(self, command):
        self.deferred_commands.append(command)

    def execute_deferred_commands(self):
        [command.execute() for command in self.deferred_commands]

# İstemci kodu
receiver, invoker = Receiver(), Invoker()

# Ertelemeli işlemi tanımla ve yürüt
invoker.add_deferred_command(DeferredCommand(receiver, "Bekletilen İşlem"))
invoker.execute_deferred_commands()
