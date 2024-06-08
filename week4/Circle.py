import matplotlib.pyplot as plt
import matplotlib.patches   # patches를 이용해 원을 그림
from .Point import Point

class Circle(Point):

    def __init__(self, x, y, r, _axes=None):
        super().__init__(x,y,_axes)
        self.r = r

    def draw(self):
        super().draw()
        c = matplotlib.patches.Circle(
            xy = (self.x,self.y),   # point로 부터 상속받음
            radius= self.r,
            fc = 'b',   # face color(원의 색) = blue
            ec = 'k',    # 원의 엣지부분 = black
        )
        self.axes.add_patch(c)
        return self.axes

if __name__ == "__main__":
    a = Circle(3,3,1)
    a.draw()
    a.show()