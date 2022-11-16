from abc import ABC, abstractmethod


class Pet(ABC):
    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Dog(Pet):
    def speak(self):
        return "Woof!"

    def __str__(self):
        return "Dog"


class Cat(Pet):
    def speak(self):
        return "Meow!"

    def __str__(self):
        return "Cat"


class Collar(ABC):
    @abstractmethod
    def __str__(self):
        pass


class LeatherCollar(Collar):
    def __str__(self):
        return "Leather Collar"


class NylonCollar(Collar):
    def __str__(self):
        return "Nylon Collar"


class PetStore:
    def __init__(self, pet_factory=None):
        self._pet_factory = pet_factory

    def show_pet(self):
        pet = self._pet_factory.get_pet()
        print("We have a lovely {}".format(pet))
        print("It says {}".format(pet.speak()))
        print("It wears a {}".format(self._pet_factory.get_collar()))


class PetFactory(ABC):
    @abstractmethod
    def get_pet(self):
        pass

    @abstractmethod
    def get_collar(self):
        pass


class DogFactory(PetFactory):
    def get_pet(self):
        return Dog()

    def get_collar(self):
        return LeatherCollar()


class CatFactory(PetFactory):
    def get_pet(self):
        return Cat()

    def get_collar(self):
        return NylonCollar()


if __name__ == "__main__":
    shop = PetStore(DogFactory())
    shop.show_pet()
    print()
    shop = PetStore(CatFactory())
    shop.show_pet()


class Chair(ABC):
    @abstractmethod
    def sit(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class ModernChair(Chair):
    def sit(self):
        return "Modern Chair"

    def __str__(self):
        return "Modern Chair"


class OldChair(Chair):
    def sit(self):
        return "Old Chair"

    def __str__(self):
        return "Old Chair"


class Sofa(ABC):
    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def lay(self):
        pass


class ModernSofa(Sofa):
    def __str__(self):
        return "Modern Sofa"

    def lay(self):
        return "Modern Sofa"


class OldSofa(Sofa):
    def __str__(self):
        return "Old Sofa"

    def lay(self):
        return "Old Sofa"


class FurnitureFactory(ABC):
    @abstractmethod
    def get_chair(self):
        pass

    @abstractmethod
    def get_sofa(self):
        pass


class ModernFurnitureFactory(FurnitureFactory):
    def get_chair(self):
        return ModernChair()

    def get_sofa(self):
        return ModernSofa()


class OldFurnitureFactory(FurnitureFactory):
    def get_chair(self):
        return OldChair()

    def get_sofa(self):
        return OldSofa()


class FurnitureStore:
    def __init__(self, furniture_factory=None):
        self._furniture_factory = furniture_factory

    def show_furniture(self):
        chair = self._furniture_factory.get_chair()
        print("We have a lovely {}".format(chair))
        print("It says {}".format(chair.sit()))
        sofa = self._furniture_factory.get_sofa()
        print("We have a lovely {}".format(sofa))
        print("It says {}".format(sofa.lay()))


if __name__ == "__main__":
    shop = FurnitureStore(ModernFurnitureFactory())
    shop.show_furniture()
    print()
    shop = FurnitureStore(OldFurnitureFactory())
    shop.show_furniture()