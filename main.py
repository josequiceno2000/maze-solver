from window import Window, Cell
from line import Point, Line

def main():
    print("Starting aMAZEment")
    win = Window(800, 600)

    # Determine Cell Size:
    cell_size = 70

    # Creating Cell Objects:
    cell1 = Cell(60, 60, 60 + cell_size, 60 + cell_size, win)
    cell1.draw()

    cell2 = Cell(300, 300, 300 + cell_size, 300 + cell_size, win)
    cell2.draw()

    # Cell Objects with Missing Walls:
    cell3 = Cell(250, 400, 250 + cell_size, 400 + cell_size, win)
    cell3.has_bottom_wall = False
    cell3.has_right_wall = False
    cell3.draw()

    cell4 = Cell(600, 150, 600 + cell_size, 150 + cell_size, win)
    cell4.has_left_wall = False
    cell4.has_right_wall = False
    cell4.draw()

    cell5 = Cell(500, 400, 500 + cell_size, 400 + cell_size, win)
    cell5.has_top_wall = False
    cell5.draw()


    win.wait_for_close()

if __name__ == "__main__":
    main()