from direct.showbase.ShowBase import ShowBase
from panda3d.core import Point3

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Load the environment model
        self.environ = self.loader.loadModel("models/environment")
        self.environ.reparentTo(self.render)
        self.environ.setScale(0.25, 0.25, 0.25)
        self.environ.setPos(-8, 42, 0)

        # Load and position a model of a jet
        self.jet = self.loader.loadModel("models/jet")
        self.jet.reparentTo(self.render)
        self.jet.setScale(0.5, 0.5, 0.5)
        self.jet.setPos(Point3(0, 10, 0))

app = MyApp()
app.run()
