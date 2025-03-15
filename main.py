import sys
from cell import Cell
from maze import Maze
from window import Window
from line import Point, Line

def main():
    print("Starting...")
    print("""
 █████╗ ███╗   ███╗ █████╗ ███████╗███████╗███╗   ███╗███████╗███╗   ██╗████████╗
██╔══██╗████╗ ████║██╔══██╗╚══███╔╝██╔════╝████╗ ████║██╔════╝████╗  ██║╚══██╔══╝
███████║██╔████╔██║███████║  ███╔╝ █████╗  ██╔████╔██║█████╗  ██╔██╗ ██║   ██║   
██╔══██║██║╚██╔╝██║██╔══██║ ███╔╝  ██╔══╝  ██║╚██╔╝██║██╔══╝  ██║╚██╗██║   ██║   
██║  ██║██║ ╚═╝ ██║██║  ██║███████╗███████╗██║ ╚═╝ ██║███████╗██║ ╚████║   ██║   
╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝   ╚═╝   
"""                                                                                 
)

    # Testing the Maze
    num_rows = int(input("How many rows should the maze have? [Enter 2 - 16]\n"))
    while num_rows < 2 or num_rows > 16:
        num_rows = int(input("\nThat's not an allowed number of rows. Try entering something between 2 and 16\n"))

    num_cols = int(input("\nExcellent. Now, how many columns? [Enter 2 - 16]\n"))
    while num_cols < 2 or num_cols > 16:
        num_cols = int(input("\nThat's not an allowed number of rows. Try entering something between 2 and 16\n"))

    margin = 40
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows

    sys.setrecursionlimit(10000)
    win = Window(screen_x, screen_y)

    print("\n\nDrawing the maze")

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win, 4)
    print("\nThe maze has been constructed")
    
    solved = maze.solve()
    if solved:
        print("\nWe have escaped the maze.")
    else:
        print("\nLost in the maze...")

    win.wait_for_close()

if __name__ == "__main__":
    main()