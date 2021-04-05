def say_hi_bro(name="bro"):
    print(f"Hi, {name}!")

if __name__ == '__main__':
    say_hi_bro("Billy")
    say_hi_bro(name="Molly")

    friend_name = "Vasya"
    say_hi_bro(friend_name)

    friend_name = input("input name: ")
    say_hi_bro(friend_name)

    say_hi_bro()