import matplotlib.pyplot as plt

class MObject:

    def __init__(self,_axes=None):
        self.figure = None
        self.axes = None
        if self.axes == None:
            if _axes == None:
                self.figure, self.axes = plt.subplots(
                    figsize=(5,5)
                )
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
        pass # to be implemented

    def __call__(self):
        return self.draw()

    def show(self):
        plt.show()