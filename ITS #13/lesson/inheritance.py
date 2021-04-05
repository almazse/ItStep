class Tree:

    def __init__(self, kind, height):
        self.kind, self.height = kind, height

    def grow(self, step=0.5):
        self.height += step

    def __str__(self):
        return f'Tree {self.kind}, height = {self.height}'


class FruitTree(Tree):

    def __init__(self, kind, height, weight):
        super().__init__(kind, height)
        self.weight = weight

    def give_fruits(self):
        print(f'we have got {self.weight}kg {self.kind}')


if __name__ == '__main__':
    oak = Tree('oak', 5.7)
    print(oak)
    oak.grow(1)
    print(oak)
    try:
        oak.give_fruits()
    except AttributeError:
        print('Parent object doesn\'t support childs methods!')

    apple_tree = FruitTree('apple', 2.2, 9)
    print(apple_tree)
    apple_tree.grow()
    print(apple_tree)
    apple_tree.give_fruits()
