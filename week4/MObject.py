import matplotlib.pyplot as plt

class MObject:

    def __init__(self,_axes=None):   # 생성자 생성, 생성자가 제일 처음, __init__: a=MObject(...), self: 메소드, _로 시작되는 것은 없어도 되는 것을 의미
        # 방법1
        self.figure = None   # 초기화
        self.axes = None   # 초기화
        if self.axes == None:
            if _axes == None:
                self.figure, self.axes = plt.subplots(
                    figsize=(5,5)
                )
                
                # 방법2
                # self.fig = plt.figure(
                #     figsize=(5,5),
                #     facecolor = 'w',
                # )
                # self.axes = self.fig.add_axes(
                #     (0.1,0.1,0.8,0.8),
                # )
            else:
                self.axes = _axes
        else:
            if _axes == None:
                pass
            else:
                self.axes = _axes

    def draw(self):
        pass # to be implemented   # 그릴게 없어서 pass

    def __call__(self):
        return self.draw()

    def show(self):
        plt.show()