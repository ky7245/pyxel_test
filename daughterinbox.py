import pyxel
from enum import Enum
# constants
one_grid = 20   # pixel per grid
offset = 20     # board between window
board_width = 4
board_height = 5

# default
#
# __     __
#| A     B |
#| E C D F |
#| E G G F |
#| H J J I |
#| H J J I |
# ---------
# x -> 0-3, y -> 0-4

class Status(Enum):
    idle = 1
    select_waiting = 2


class Obj:
    def __init__(self, posx, posy, width, height):
        self.x = posx
        self.y = posy
        self.width = width
        self.height = height
        self.onMouse = False
        self.onClick = False
    
    def point_upperleft_x(self):
        return self.x * one_grid + 1

    def point_upperleft_y(self):
        return self.y * one_grid + 1

    def point_lowerright_x(self):
        return self.point_upperleft_x() + self.width * one_grid - 2

    def point_lowerright_y(self):
        return self.point_upperleft_y() + self.height * one_grid -2
    
    def isIncludes(self, px, py):
        if self.point_upperleft_x() <= px <= self.point_lowerright_x() and \
         self.point_upperleft_y() <= py <= self.point_lowerright_y():
            return True
        return False

class Board:
    def __init__(self):
        self.table = [[0 for _ in range(board_width)] for _ in range(board_height)]
        self.stat = Status.idle
        self.objs = [ 
            Obj(0, 0, 1, 1),
            Obj(3, 0, 1, 1),
            Obj(1, 1, 1, 1),
            Obj(2, 1, 1, 1),
            Obj(0, 1, 1, 2),
            Obj(3, 1, 1, 2),
            Obj(1, 2, 2, 1),
            Obj(0, 3, 1, 2),
            Obj(3, 3, 1, 2),
            Obj(1, 3, 2, 2)
        ]
    
    def __repr__(self):
        ret = ''
        for row in self.table:
            for g in row:
                ret += str(g)
            ret += '\n'
        return ret

    # public method
    def draw(self):
        for obj in self.objs:
            x1 = obj.point_upperleft_x() + offset
            y1 = obj.point_upperleft_y() + offset
            x2 = obj.point_lowerright_x() + offset
            y2 = obj.point_lowerright_y() + offset
            col = 5
            if obj.onMouse:
                col = 6
                if obj.onClick:
                    col = 7
                obj.onMouse = False
                obj.onClick = False

            pyxel.rect(x1, y1, x2, y2, col)
    
    def update(self):
        pass
    
    def onMouse(self, mx, my):
        for obj in self.objs:
            if obj.isIncludes(mx, my):
                obj.onMouse = True
    
    def onClick(self, mx, my):
        for obj in self.objs:
            if obj.isIncludes(mx, my):
                obj.onClick = True

    # private method


class App:
    def __init__(self):
        self.board = Board()

        pyxel.init(120, 140)
        pyxel.mouse(True)
        pyxel.run(self.update, self.draw)



    def update(self):
        mx, my = pyxel.mouse_x, pyxel.mouse_y

        # base at upper left
        bx = mx - offset
        by = my - offset

        print(mx, my, bx, by)

        if 0 <= bx <= one_grid*board_width and \
            0 <= by <= one_grid*board_height:   # on board
            if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
                self.board.onClick(bx, by)
            else:
                self.board.onMouse(bx, by)

        self.board.update()




    def draw(self):
        pyxel.cls(0)
        pyxel.rectb(20, 20, 100, 120, 9)

        self.board.draw()


App()