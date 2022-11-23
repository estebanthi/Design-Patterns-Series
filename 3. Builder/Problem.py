from abc import ABC, abstractmethod


class Computer(ABC):

    def __init__(self, case, mainboard, cpu):
        self.case = case
        self.mainboard = mainboard
        self.cpu = cpu

    def __str__(self):
        return f'{self.case} {self.mainboard} {self.cpu}'


class GamingComputer(Computer):
    def __init__(self):
        super().__init__('Coolermaster N300', 'MSI 970', 'Intel Core i7')


class OfficeComputer(Computer):
    def __init__(self):
        super().__init__('Coolermaster N300', 'MSI 970', 'Intel Core i5')


if __name__ == '__main__':
    print(GamingComputer())
    print(OfficeComputer())
