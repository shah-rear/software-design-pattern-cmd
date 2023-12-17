from abc import ABC, abstractmethod
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass
class ConcreteCommandA(Command):
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.perform_operation_A()
class Receiver:
    def perform_operation_A(self):
        print("Receiver is performing Operation A")
class Invoker:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def execute_command(self):
        self.command.execute()
# Client code
receiver, concrete_command, invoker = Receiver(),
ConcreteCommandA(Receiver()), Invoker()
invoker.set_command(concrete_command)
invoker.execute_command()
