import copy
import time


class Prototype:
    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        self._objects[name] = obj

    def unregister_object(self, name):
        del self._objects[name]

    def clone(self, name, **attr):
        obj = self._objects.get(name)
        if not obj:
            raise ValueError('Incorrect object name: {}'.format(name))
        obj = copy.deepcopy(obj)
        obj.__dict__.update(attr)
        return obj


class Monster:
    def __init__(self, name, health, damage):
        time.sleep(1)
        self.name = name
        self.health = health
        self.damage = damage

    def __eq__(self, other):
        return self.name == other.name and self.health == other.health and self.damage == other.damage


if __name__ == '__main__':
    time_start = time.time()

    orc = Monster('Orc', 100, 10)

    prototype = Prototype()
    prototype.register_object('orc', orc)

    orcs = [prototype.clone('orc') for _ in range(10)]

    time_end = time.time()

    print("Time to copy: {} seconds".format(time_end - time_start))
    print(f"All orcs are equal: {all([orc == orc2 for orc2 in orcs])}")

    pyromancer = Monster('Pyromancer', 150, 10)
    black_knight = Monster('Black Knight', 290, 20)
    mega_orc = Monster('Mega Orc', 500, 50)

    prototype.register_object('pyromancer', pyromancer)
    prototype.register_object('black_knight', black_knight)
    prototype.register_object('mega_orc', mega_orc)

    pyromancers = [prototype.clone('pyromancer') for _ in range(50)]
    black_knights = [prototype.clone('black_knight') for _ in range(20)]
    mega_orcs = [prototype.clone('mega_orc') for _ in range(3)]