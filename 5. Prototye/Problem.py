import time


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
    orcs = [Monster('Orc', 100, 10) for _ in range(10)]

    time_end = time.time()

    print("Time to copy: {} seconds".format(time_end - time_start))
    print(f"All orcs are equal: {all([orc == orc2 for orc2 in orcs])}")