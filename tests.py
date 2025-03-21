import unittest
from maze import Maze
from cell import Cell

class TestMaze(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 20
        num_rows = 10
        maze1 = Maze(0, 0, num_rows, num_cols, 20, 20)
        
        self.assertEqual(
            len(maze1._cells),
            num_cols
        )
        self.assertEqual(
            len(maze1._cells[0]),
            num_rows
        )
        self.assertEqual(
            len(maze1._cells[-1]),
            num_rows
        )
    
    def test_maze_create_cells_larger(self):
        num_cols = 20
        num_rows = 18
        maze2 = Maze(50, 50, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(maze2._cells),
            num_cols,
        )
        self.assertEqual(
            len(maze2._cells[1]),
            num_rows,
        )
    
    def test_maze_dimmensions(self):
        num_cols = 15
        num_rows = 5
        cell_size = 30
        maze = Maze(10, 10, num_rows, num_cols, cell_size, cell_size)
        self.assertEqual(
            maze._num_rows,
            num_rows
        )
        self.assertEqual(
            maze._num_cols,
            num_cols
        )
        self.assertEqual(
            maze._cell_size_x,
            cell_size
        )
        self.assertEqual(
            maze._cell_size_y,
            cell_size
        )

    def test_reset_cells_visited(self):
        num_cols = 10
        num_rows = 14
        cell_size = 40
        maze = Maze(50, 50, num_rows, num_cols, cell_size, cell_size, seed=3)
        
        for col in maze._cells:
            for cell in col:
                self.assertFalse(cell._visited)
    
    def test_break_entrance_and_exit(self):
        num_cols = 15
        num_rows = 5
        cell_size = 30
        maze = Maze(10, 10, num_rows, num_cols, cell_size, cell_size)
        maze._break_entrance_and_exit()
        self.assertFalse(maze._cells[0][0].has_top_wall)
        self.assertFalse(maze._cells[-1][-1].has_bottom_wall)


class TestCell(unittest.TestCase):
    def test_cell_creation(self):
        cell = Cell(18, 20, 24, 40)
        self.assertTrue(cell.has_top_wall)
        self.assertTrue(cell.has_right_wall)
        self.assertTrue(cell.has_bottom_wall)
        self.assertTrue(cell.has_left_wall)
        self.assertEqual(
            cell._x1,
            18
        )
        self.assertEqual(
            cell._y1,
            20
        )
        self.assertEqual(
            cell._x2,
            24
        )
        self.assertEqual(
            cell._y2,
            40
        )

    def test_cell_remove_walls(self):
        cell = Cell(10, 30, 20, 60)
        cell.has_bottom_wall = False
        cell.has_top_wall = False
        self.assertFalse(cell.has_top_wall)
        self.assertTrue(cell.has_right_wall)
        self.assertFalse(cell.has_bottom_wall)
        self.assertTrue(cell.has_left_wall)


if __name__ == "__main__":
    unittest.main()