def make_friends(boy_name, girl_name):
    print(f"{boy_name} и {girl_name} - друзья навеки")

def make_lovers(man_name, woman_name="Анджелина"):
    print(f"{man_name} и {woman_name} - жених и невеста")


if __name__ == '__main__':
    make_friends("Вася", "Даша")

    make_friends(boy_name="Вася", girl_name="Даша")
    make_friends(girl_name="Даша", boy_name="Вася")

    make_lovers("Брэд")
    make_lovers("Брэд", "Дженнифер")

