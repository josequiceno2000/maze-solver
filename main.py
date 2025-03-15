from cell import Cell
from maze import Maze
from window import Window
from line import Point, Line

def main():
    print("Starting aMAZEment")

    # Testing the Maze
    num_rows = 14
    num_cols = 6
    margin = 40
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)
    maze._break_entrance_and_exit()


    win.wait_for_close()

if __name__ == "__main__":
    main()