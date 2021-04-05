from sort_obj import Kitty

DATA = (
    ('Bony', 10),
    ('Tom', 9),
    ('Kate', 7),
    ('Tom', 5),
)


def test_kitty_start():
    bony = Kitty(*DATA[0])
    assert isinstance(bony, Kitty)


def test_sorted_kitties():
    kitties = [Kitty(*kitty) for kitty in DATA]
    is_kitties = [isinstance(kitty, Kitty) for kitty in kitties]
    sorted_kitties = sorted(kitties)
    assert all(is_kitties) is True
    assert sorted_kitties[0]._age == 5
    assert sorted_kitties[-1]._age == 10
