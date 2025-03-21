from tkinter import Tk, BOTH, Canvas
from line import Point, Line


class Window:

    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("aMAZEment")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=True)
        self.__window_running = False
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__window_running = True
        while self.__window_running:
            self.redraw()
        print("The maze is collapsing...")

    def close(self):
        self.__window_running = False

    # Drawing methods
    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)


