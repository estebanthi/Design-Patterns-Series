class Dog:
    def speak(self):
        return "Woof!"
    def __str__(self):
        return "Dog"


class PetStore:
    def __init__(self, pet):
        self._pet = pet

    def show_pet(self):
        print("We have a lovely {}".format(self._pet))
        print("It says {}".format(self._pet.speak()))


if __name__ == "__main__":
    dog = Dog()
    shop = PetStore(dog)
    shop.show_pet()