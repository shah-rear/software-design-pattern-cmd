from abc import ABC, abstractmethod
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass
class ConcreteCommandA(Command):
    def execute(self):
        print("Executing Command A")
class ConcreteCommandB(Command):
    def execute(self):
        print("Executing Command B")

class Receiver:
    def perform_operation_A(self):
        print("Receiver is performing Operation A")
class Invoker:
    def __init__(self, commands=[]):
        self.commands = commands

    def add_command(self, command):
        self.commands.append(command)

    def execute_commands(self):
        [command.execute() for command in self.commands]
# Client code
receiver = Receiver()
invoker = Invoker([ConcreteCommandA(), ConcreteCommandB()])

invoker.execute_commands()
