class FirstSimpleObject:
    pass


class Animal:
    def __init__(self, name, number_of_eyes, number_of_laps, tail=True):
        self.name = name
        self.number_of_eyes = number_of_eyes
        self.number_of_laps = number_of_laps
        self.tail = tail

    def make_noize(self):
        return f'I\'m {self.name}'


class Car:
    def __init__(self, brand_name, model_name, color, wheel_d, engine_volume):
        self.brand_name = brand_name
        self.model_name = model_name
        self.color = color
        self.wheel_d = wheel_d
        self.engine_volume = engine_volume


if __name__ == '__main__':
    simple_first_class_object = FirstSimpleObject()
    giraffe = Animal('giraffe', 2, 4)
    print(f'GIRAFFE object: {giraffe.name} '
          f'{giraffe.number_of_eyes} {giraffe.number_of_laps} '
          f'{giraffe.tail}')

    print(giraffe.make_noize())

    bmw_color_blue = Car('bmw', '525', 'blue', 21, 2.0)
    print(f'Brand: {bmw_color_blue.brand_name}\n'
          f'model: {bmw_color_blue.model_name}\n'
          f'color: {bmw_color_blue.color}\n'
          f'wheel size: {bmw_color_blue.wheel_d}\n'
          f'engine volume: {bmw_color_blue.engine_volume}')

    try:
        bmw_color_blue = Car('bmw', '525', 'blue', 21)
    except TypeError:
        print('car can\'t be created')