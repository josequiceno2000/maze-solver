import time
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
            win
        ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        self._create_cells()

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
        cell = self._cells[col][row]
        cell.draw()
        self._animate()
    
    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.04)