import matplotlib.pyplot as plt
import matplotlib
import oop.Circle
import oop.Point

def test_external_axes():
    fig,axes = plt.subplots(figsize=(10,10))
    a = oop.Point.Point(2,2,axes)
    axes = a.draw()
    b = oop.Circle.Circle(4,4,2,axes)
    b.draw()
    plt.show()

def test_internal_axes():
    a = oop.Point.Point(2,2)
    axes = a.draw()
    b = oop.Circle.Circle(4,4,2,axes)
    b.draw()
    b.show()

if __name__ == "__main__":
    print(matplotlib.__version__)
    # test_external_axes()
    test_internal_axes()