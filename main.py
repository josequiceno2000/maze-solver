from window import Window
from line import Point, Line

def main():
    print("Starting aMAZEment")
    win = Window(800, 600)

    # Point Objects
    point1 = Point(70, 70)
    point2 = Point(25, 74)
    point3 = Point(106, 509)
    point4 = Point(300, 300)
    point5 = Point(212, 46)

    # Line Objects:
    line1 = Line(point3, point1)
    line2 = Line(point5, point1)
    line3 = Line(point2, point1)
    line4 = Line(point5, point4)

    # Drawing the Lines:
    win.draw_line(line1, "orange")
    win.draw_line(line2, "purple")
    win.draw_line(line3, "red")
    win.draw_line(line4, "black")

    win.wait_for_close()

if __name__ == "__main__":
    main()