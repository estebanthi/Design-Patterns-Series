from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

    @abstractmethod
    def redo(self):
        pass


class DispenseCommand(Command):
    def __init__(self, vending_machine, product_code):
        self.vm = vending_machine
        self.product_code = product_code

    def execute(self):
        self.vm.dispense(self.product_code)

    def undo(self):
        self.vm.refill(self.product_code)

    def redo(self):
        self.execute()


class VendingMachine:
    def __init__(self):
        self.inventory = {"cola": 5, "water": 10, "juice": 8}

    def dispense(self, product_code):
        if product_code not in self.inventory:
            print(f"Product {product_code} is not available")
            return
        if self.inventory[product_code] == 0:
            print(f"Product {product_code} is out of stock")
            return
        self.inventory[product_code] -= 1
        print(f"Dispensing product {product_code}")

    def refill(self, product_code):
        if product_code not in self.inventory:
            print(f"Product {product_code} is not available")
            return
        self.inventory[product_code] += 1
        print(f"Refilling product {product_code}")


class VendingMachineController:
    def __init__(self, vending_machine):
        self.vm = vending_machine
        self.commands = []

    def add_command(self, command):
        self.commands.append(command)

    def execute_commands(self):
        for command in self.commands:
            command.execute()

    def undo_commands(self):
        for command in reversed(self.commands):
            command.undo()

    def redo_commands(self):
        for command in self.commands:
            command.redo()

    def clear_commands(self):
        self.commands = []


if __name__ == "__main__":
    vm = VendingMachine()
    controller = VendingMachineController(vm)
    controller.add_command(DispenseCommand(vm, "cola"))
    controller.add_command(DispenseCommand(vm, "cola"))
    controller.add_command(DispenseCommand(vm, "cola"))
    controller.add_command(DispenseCommand(vm, "cola"))
    controller.add_command(DispenseCommand(vm, "cola"))
    controller.add_command(DispenseCommand(vm, "cola"))
    controller.add_command(DispenseCommand(vm, "cola"))

    print("Executing commands")
    controller.execute_commands()

    print("Undoing commands")
    controller.undo_commands()

    print("Redoing commands")
    controller.redo_commands()

    controller.clear_commands()

    print("Executing commands")
    controller.execute_commands()
