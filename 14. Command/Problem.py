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


if __name__ == "__main__":
    vm = VendingMachine()
    vm.dispense("cola")
    vm.dispense("cola")
    vm.dispense("cola")
    vm.dispense("cola")
    vm.dispense("cola")
    vm.dispense("cola")
    vm.dispense("cola")