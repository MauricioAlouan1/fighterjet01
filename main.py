from direct.showbase.ShowBase import ShowBase
from panda3d.core import Point3, KeyboardButton

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Load the environment model
        self.environ = self.loader.loadModel("models/environment")
        self.environ.reparentTo(self.render)
        self.environ.setScale(0.25, 0.25, 0.25)
        self.environ.setPos(-8, 42, 0)

        # Load and position a model of a panda as a placeholder for the jet
        self.jet = self.loader.loadModel("models/seahawk.egg")
        self.jet.reparentTo(self.render)
        self.jet.setScale(0.1, 0.1, 0.1)  # Make the panda smaller
        self.jet.setPos(Point3(0, 10, 10))

        # Set initial position
        self.jet.setPos(0, 10, 0)

        # Disable the default camera control to handle it manually
        self.disableMouse()

        # Update task to move the panda
        self.taskMgr.add(self.update, "update")

        # Keyboard control setup
        self.accept("arrow_left", self.move_left)
        self.accept("arrow_right", self.move_right)
        self.accept("arrow_up", self.move_up)
        self.accept("arrow_down", self.move_down)
        self.accept(";", self.increase_speed)
        self.accept("/", self.decrease_speed)
        self.accept("w", self.camera_up)
        self.accept("s", self.camera_down)
        self.accept("a", self.camera_left)
        self.accept("d", self.camera_right)

        # Movement step size
        self.move_step = 0.5
        # Initial forward speed
        self.forward_speed = 0.1
        # Camera movement step size
        self.camera_step = 0.5

    def update(self, task):
        # Move the jet forward
        self.jet.setY(self.jet, self.forward_speed)

        # Camera follow the jet
        self.camera.lookAt(self.jet)
        return task.cont

    def move_left(self):
        self.jet.setX(self.jet.getX() - self.move_step)

    def move_right(self):
        self.jet.setX(self.jet.getX() + self.move_step)

    def move_up(self):
        self.jet.setZ(self.jet.getZ() + self.move_step)

    def move_down(self):
        self.jet.setZ(self.jet.getZ() - self.move_step)

    def increase_speed(self):
        self.forward_speed += 0.1

    def decrease_speed(self):
        self.forward_speed = max(0, self.forward_speed - 0.1)

    def camera_up(self):
        self.camera.setZ(self.camera, self.camera_step)

    def camera_down(self):
        self.camera.setZ(self.camera, -self.camera_step)

    def camera_left(self):
        self.camera.setX(self.camera, -self.camera_step)

    def camera_right(self):
        self.camera.setX(self.camera, self.camera_step)

app = MyApp()
app.run()
