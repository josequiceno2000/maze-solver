from line import Line, Point

class Cell:
    def __init__(
            self, 
            x1, 
            y1, 
            x2, 
            y2, 
            win=None
        ):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._win = win

    def draw(self):
        if self.has_left_wall:
            self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x1, self._y2)))
        if self.has_top_wall:
            self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x2, self._y1)))
        if self.has_right_wall:
            self._win.draw_line(Line(Point(self._x2, self._y1), Point(self._x2, self._y2)))
        if self.has_bottom_wall:
            self._win.draw_line(Line(Point(self._x1, self._y2), Point(self._x2, self._y2)))
    
    def draw_move(self, to_cell, undo=False):
        # Set color
        fill_color = "red"
        if undo:
            fill_color = "gray"

        # Get center of this cell
        this_center_x = (self._x1 + self._x2) // 2
        this_center_y = (self._y1 + self._y2) // 2

        # Get center for other cell
        to_center_x = (to_cell._x1 + to_cell._x2) // 2
        to_center_y = (to_cell._y1 + to_cell._y2) // 2

        # Draw line
        center_line = Line(Point(this_center_x, this_center_y), Point(to_center_x, to_center_y))
        self._win.draw_line(center_line, fill_color)
        

