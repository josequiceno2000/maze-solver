from window import Window, Cell
from line import Point, Line

def main():
    print("Starting aMAZEment")
    win = Window(800, 600)

    # Line Objects:
    line1 = Line(Point(106, 509), Point(70, 70))
    line2 = Line(Point(212, 46), Point(70, 70))
    line3 = Line(Point(25, 74), Point(70, 70))
    line4 = Line(Point(212, 46), Point(300, 300))

    # Drawing the Lines:
    win.draw_line(line1, "orange")
    win.draw_line(line2, "purple")
    win.draw_line(line3, "red")
    win.draw_line(line4, "black")

    win.wait_for_close()

if __name__ == "__main__":
    main()