from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

class ConcreteCommand(Command):
    def __init__(self, receiver, action):
        self.receiver, self.action = receiver, action

    def execute(self):
        print(f"Performing action: {self.action}")
        self.receiver.state += 1

    def undo(self):
        print(f"Undoing action: {self.action}")
        self.receiver.state -= 1

class Receiver:
    def __init__(self):
        self.state = 0

class Invoker:
    def __init__(self):
        self.command_stack, self.undo_stack = [], []

    def execute_command(self, command):
        command.execute()
        self.command_stack.append(command)

    def undo_last_command(self):
        if self.command_stack:
            self.undo_stack.append(self.command_stack.pop().undo())

    def redo_last_undo(self):
        if self.undo_stack:
            self.execute_command(self.undo_stack.pop())

# Client code
receiver, invoker = Receiver(), Invoker()

# Execute commands
command1 = ConcreteCommand(receiver, "Action 1")
command2 = ConcreteCommand(receiver, "Action 2")

invoker.execute_command(command1)
invoker.execute_command(command2)

# Undo the last command
invoker.undo_last_command()

# Redo the undone command
invoker.redo_last_undo()
