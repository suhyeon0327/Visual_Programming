import matplotlib.pyplot as plt
import matplotlib.patches
from .Point import Point

class Circle(Point):

    def __init__(self, x, y, r, _axes=None):
        super().__init__(x,y,_axes)
        self.r = r

    def draw(self):
        super().draw()
        c = matplotlib.patches.Circle(
            xy = (self.x,self.y),
            radius= self.r,
            fc = 'b',
            ec = 'k', 
        )
        self.axes.add_patch(c)
        return self.axes

if __name__ == "__main__":
    a = Circle(3,3,1)
    a.draw()
    a.show()