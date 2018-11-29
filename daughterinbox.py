import pyxel

# pixel per grid
one_grid = 20
offset = 20

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



class Obj:
    def __init__(self, posx, posy, width, height):
        self.x = posx
        self.y = posy
        self.width = width
        self.height = height
        self.onMouse = False
        self.onClick = False
    
    def point_upperleft_x(self):
        return self.x * one_grid + 1 + offset

    def point_upperleft_y(self):
        return self.y * one_grid + 1 + offset

    def point_lowerright_x(self):
        return self.point_upperleft_x() + self.width * one_grid - 2

    def point_lowerright_y(self):
        return self.point_upperleft_y() + self.height * one_grid -2
    
    def isIncludes(self, px, py):
        if self.point_upperleft_x() <= px <= self.point_lowerright_x() and \
         self.point_upperleft_y() <= py <= self.point_lowerright_y():
            return True
        return False

class App:
    def __init__(self):
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

        pyxel.init(120, 140)
        pyxel.mouse(True)
        pyxel.run(self.update, self.draw)


    def update(self):
        mx, my = pyxel.mouse_x, pyxel.mouse_y
        print(mx, my)
        for obj in self.objs:
            if obj.isIncludes(mx, my):
                obj.onMouse = True
                if pyxel.btn(pyxel.MOUSE_LEFT_BUTTON):
                    obj.onClick = True



    def draw(self):
        pyxel.cls(0)
        pyxel.rectb(20, 20, 100, 120, 9)
        for obj in self.objs:
            x1 = obj.point_upperleft_x()
            y1 = obj.point_upperleft_y()
            x2 = obj.point_lowerright_x()
            y2 = obj.point_lowerright_y()
            col = 5
            if obj.onMouse:
                col = 6
                if obj.onClick:
                    col = 7
                obj.onMouse = False
                obj.onClick = False

            pyxel.rect(x1, y1, x2, y2, col)

App()