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
        self.axes.plot(self.x, self.y, marker='o', c='r')   # c(color) = red
        return self.axes   # point와 circle외에 그려지지는 것들을 공유하기 위해서


if __name__ == "__main__":
    a = Point(3,3)
    a.draw()
    a.show()   # point를 메인 스트립트로 사용할 경우