import matplotlib.pyplot as plt
from .MObject import MObject

class Point(MObject):

    def __init__(self, x, y, _axes=None):
        super().__init__(_axes)
        self.x = x
        self.y = y
        if _axes != None:
            self.axes = _axes

    def draw(self):
        self.axes.plot(self.x, self.y, marker='o', c='r')
        return self.axes


if __name__ == "__main__":
    a = Point(3,3)
    a.draw()
    a.show()