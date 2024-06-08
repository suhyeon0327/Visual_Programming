import matplotlib.pyplot as plt   # plt는 별칭
import matplotlib
from .Circle import Circle   # oop라는 패키지 안에 circle, point가 있음
from .Point import Point

def test_external_axes():   # axes는 container
    fig,axes = plt.subplots(figsize=(10,10))
    a = Point(2,2,axes)
    axes = a.draw()
    b = Circle(4,4,2,axes)   # 같은 곳에 그려라
    b.draw()
    plt.show()  
    # 다른 사람과 같이 쓸때

def test_internal_axes():
    a = Point(2,2)
    axes = a.draw()
    b = Circle.Circle(4,4,2,axes)
    b.draw()
    b.show()   # 자체적으로 그리는 것
    # 내가 편가헤 쓸때

if __name__ == "__main__":
    print(matplotlib.__version__)
    # test_external_axes()
    test_internal_axes()