from tkinter import *
import winsound


main = Tk()

main.attributes('-fullscreen', 1)

WIDTH = main.winfo_screenwidth()
HEIGHT = main.winfo_screenheight()
canvas = Canvas(width=WIDTH, height=HEIGHT, highlightthickness=0)
canvas.grid(row=0, column=0)

# background
bg = PhotoImage(file='bg.png')
canvas.create_image(WIDTH / 2, HEIGHT / 2, image=bg, anchor="center", tag="bg")


def start_game(e=""):
    stop_music()
    delete_menu()
    for j in range(0, 5):
        for i in range(0, 10):

            canvas.create_rectangle(i * WIDTH // 10+10, j * HEIGHT // 5+10,
                                    i * WIDTH // 10 + WIDTH // 10 - 10, j * HEIGHT // 5 + HEIGHT // 5 - 10,
                                    fill="blue", tags=f"{i}_{j}")
            canvas.create_text((i * WIDTH // 10) + (WIDTH // 10) / 2, (j * HEIGHT // 5) + (HEIGHT // 5) / 2, text=f"{i}_{j}", font=("Arial", 15))


def stop_music(e=""):
    winsound.PlaySound(None, winsound.SND_PURGE)


def start_music(e=""):
    winsound.PlaySound("bg.wav", winsound.SND_ASYNC)

def delete_menu():
    canvas.delete("new_game")


new_game_hover = PhotoImage(file='img/menu/new_hame_hover.png')


def menu_enter(e, item):
    canvas.delete("new_game")
    canvas.create_image(WIDTH / 2, HEIGHT / 2 - 200, image=new_game_hover, anchor="center", tag="menu", tags="new_game")


new_game = PhotoImage(file='img/menu/new_game.png')


def create_menu():
    canvas.create_image(WIDTH / 2, HEIGHT / 2 - 200, image=new_game, anchor="center", tag="menu", tags="new_game")


canvas.tag_bind("new_game", "<Button-1>", start_game)
canvas.tag_bind("new_game", "<Enter>", lambda event="", item="new_game": menu_enter(event, item))


create_menu()
start_music()

main.mainloop()
