import time
import random
from cell import Cell
from line import Point, Line

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None,
            seed=None
        ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed:
            random.seed(seed)


        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        for col in range(self._num_cols):
            cells_col = []
            for row in range(self._num_rows):
                x1 = self._x1 + col * self._cell_size_x
                y1 = self._y1 + row * self._cell_size_y
                x2 = x1 + self._cell_size_x
                y2 = y1 + self._cell_size_y
                cells_col.append(Cell(x1, y1, x2, y2, self._win))
            self._cells.append(cells_col)

        # Draw all cells after
        for col in range(self._num_cols):
            for row in range(self._num_rows):
                self._draw_cell(row, col)
    
    def _draw_cell(self, row, col):
        if self._win is None:
            return
        cell = self._cells[col][row]
        cell.draw()
        self._animate()
    
    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.038)

    def _break_entrance_and_exit(self):
        # Find the entrance and exit cells
        entrance_cell = self._cells[0][0]
        exit_cell = self._cells[-1][-1]

        # Remove the outer walls and draw
        entrance_cell.has_top_wall = False
        self._draw_cell(0, 0)

        exit_cell.has_bottom_wall = False
        self._draw_cell(self._num_rows - 1, self._num_cols - 1)

    def _break_walls_r(self, col, row):
        # Mark current cell as visited
        current_cell =  self._cells[col][row]
        current_cell._visited = True

        # Infinite loop
        while True:
            possible_directions = []
            left_cell = None
            right_cell = None
            top_cell = None
            bottom_cell = None
            # Check all possible directions for cells:
            # Left Gang
            if col >= 1:
                left_cell = self._cells[col - 1][row]
                if not left_cell._visited:
                    possible_directions.append(left_cell)
                    
            # Right Gang
            if col < self._num_cols - 1:
                right_cell = self._cells[col + 1][row]
                if not right_cell._visited:
                    possible_directions.append(right_cell)

            # Top Gang
            if row >= 1:
                top_cell = self._cells[col][row - 1]
                if not top_cell._visited:
                    possible_directions.append(top_cell)

            # Bottom Gang:
            if row < self._num_rows - 1:
                bottom_cell = self._cells[col][row + 1]
                if not bottom_cell._visited:
                    possible_directions.append(bottom_cell)

            # Check if there is nowhere left to go:
            if len(possible_directions) < 1:
                self._draw_cell(row, col)
                return 
            
            # Or pick a random direction
            else:
                next_cell = random.choice(possible_directions)
                next_row = row
                next_col = col
                # Break down the walls between current and next cells
                if left_cell is not None and next_cell == left_cell:
                    current_cell.has_left_wall = False
                    next_cell.has_right_wall = False
                    next_col = col - 1
                elif top_cell is not None and next_cell == top_cell:
                    current_cell.has_top_wall = False
                    next_cell.has_bottom_wall = False
                    next_row = row - 1
                elif right_cell is not None and next_cell == right_cell:
                    current_cell.has_right_wall = False
                    next_cell.has_left_wall = False
                    next_col = col + 1
                elif bottom_cell is not None and next_cell == bottom_cell:
                    next_row = row + 1
                    current_cell.has_bottom_wall = False
                    next_cell.has_top_wall = False
            
            # Redraw the cells involved
            self._draw_cell(col=col, row=row)
            self._draw_cell(col=next_col, row=next_row)
            
            # Move to next cell with recursion
            self._break_walls_r(next_col, next_row)
                
    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell._visited = False

    # Solving the Maze
    def solve(self):
        return self._solve_r(col=0, row=0)
        
    def _solve_r(self, col, row):
        # Call the animate method
        self._animate()

        # Mark the current cell as visited
        current_cell = self._cells[col][row]
        current_cell._visited = True

        # If this is the end cell, return True
        if current_cell == self._cells[-1][-1]:
            return True
        
        # Check each direction
        next_cell = None

        # Left gang
        if (
            (col >= 1) and
            (not current_cell.has_left_wall) and
            (not self._cells[col - 1][row]._visited)
        ):
            next_cell = self._cells[col - 1][row]
            current_cell.draw_move(next_cell)
            if self._solve_r(col - 1, row):
                return True
            else:
                current_cell.draw_move(next_cell, undo=True)
        
        # Right gang
        if (
            (col < self._num_cols - 1) and
            (not current_cell.has_right_wall) and
            (not self._cells[col + 1][row]._visited)
        ):
            next_cell = self._cells[col + 1][row]
            current_cell.draw_move(next_cell)
            if self._solve_r(col + 1, row):
                return True
            else:
                current_cell.draw_move(next_cell, undo=True)

        # Top gang
        if (
            (row >= 1) and
            (not current_cell.has_top_wall) and
            (not self._cells[col][row - 1]._visited)
        ):
            next_cell = self._cells[col][row - 1]
            current_cell.draw_move(next_cell)
            if self._solve_r(col, row - 1):
                return True
            else:
                current_cell.draw_move(next_cell, undo=True)
        
        # Bottom gang
        if (
            (row < self._num_rows - 1) and
            (not current_cell.has_bottom_wall) and
            (not self._cells[col][row + 1]._visited)
        ):
            next_cell = self._cells[col][row + 1]
            current_cell.draw_move(next_cell)
            if self._solve_r(col, row + 1):
                return True
            else:
                current_cell.draw_move(next_cell, undo=True)
        
        # If no directions worked out, return False:
        return False
