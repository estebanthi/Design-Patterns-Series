import time
from unittest.mock import Mock
import random

Image = Mock()
Image.open = lambda image: time.sleep(0.00001)


class TreeTexture:
    def __init__(self, file_path):
        self.texture = Image.open(file_path)


# Create a single instance of the shared texture
tree_texture = TreeTexture('tree_texture.png')


class Tree:
    def __init__(self, x, y, size, type):
        self.x = x
        self.y = y
        self.size = size
        self.type = type
        self.texture = tree_texture


if __name__ == "__main__":
    time_start = time.time()

    trees = []
    for i in range(100):
        x = random.randint(0, 1000)
        y = random.randint(0, 1000)
        size = random.randint(1, 10)
        type = random.choice(['Oak', 'Maple', 'Pine'])
        trees.append(Tree(x, y, size, type))

    time_end = time.time()
    print(f"Time taken: {time_end - time_start}")
