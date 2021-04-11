import socket
import tkinter as tk
import json


def start_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('localhost', 8354))
    while True:
        try:
            result = s.recv(1024)
            print(f'message from: {result.decode("utf-8")}')
            dict_from_msg = json.loads(result.decode('utf-8'))
            x = dict_from_msg['x']
            y = dict_from_msg['y']
            r = dict_from_msg['r']
            color = dict_from_msg['color']
            canvas.create_oval(x - r, y - r, x + r, y + r, fill=color)
            root.update()
            s.close()
        except KeyboardInterrupt:
            break


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('+0+0')
    canvas = tk.Canvas(root, height=600, width=800)
    canvas.pack()
    button_start = tk.Button(root, text="start_server")
    button_start.pack()
    button_start.config(command=start_server)
    root.mainloop()
