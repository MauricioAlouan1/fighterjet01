from panda3d.core import Point3

def load_jet(app):
    jet = app.loader.loadModel("models/jet01.egg")
    jet.reparentTo(app.render)
    jet.setScale(0.1, 0.1, 0.1)
    jet.setPos(Point3(0, 0, 5))
    return jet
