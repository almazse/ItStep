import time
import random
import threading
import tkinter as tk

TK_HEIGHT = 500
TK_WIDTH = 600
COLORS = ['blue',
          'red',
          'green',
          'orange',
          'white',
          'black',
          'brown']

class MyRootTK:

    @staticmethod
    def __doc__():
        return "This canvas root class"

    def __init__(self, root: tk.Tk):
        self.root = root
        self.canvas = tk.Canvas(self.root, width=TK_WIDTH, height=TK_HEIGHT)
        self.canvas.pack()
        self.button = tk.Button(text='Start', command=self.click)
        self.button.pack()

    def draw_circle(self, x, y, radius, color):
        """
        Draw circle on the Canvas object
        :return: None
        """

        self.canvas.create_oval(
            x-radius, y-radius, x+radius, y+radius, fill=color
        )

    def click(self):
        """
        :return:
        """
        print('click')
        t = MyThread(self)
        t.start()

class MyThread(threading.Thread):
    id = 0

    def __init__(self, myroot: MyRootTK):
        MyThread.id += 1
        name = f'My Thread No{MyThread.id}'
        threading.Thread.__init__(self, name=name)
        self.myroot = myroot

    def run(self):
        print(f'{threading.currentThread().getName()} started')
        for color in COLORS:
            time.sleep(0.5)
            x = random.randint(0, TK_WIDTH)
            y = random.randint(0, TK_HEIGHT)
            radius = random.randint(5, 25)
            self.myroot.draw_circle(x, y, radius, color)
            print(f'{threading.currentThread().getName()} finishied')


if __name__ == '__main__':
    root = tk.Tk()
    myroot = MyRootTK(root)
    root.mainloop()