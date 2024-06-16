from direct.showbase.ShowBase import ShowBase
from panda3d.core import Point3

from terrain import load_terrain
from jet import load_jet
from controls import setup_controls
from camera import setup_camera, update_camera

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Load the terrain
        self.terrain = load_terrain(self)

        # Load and position the jet
        self.jet = load_jet(self)

        # Disable the default camera control to handle it manually
        self.disableMouse()

        # Set initial camera position
        self.camera_offset = setup_camera(self)

        # Update task to move the jet
        self.taskMgr.add(self.update, "update")

        # Keyboard control setup
        self.keys = setup_controls(self)

        # Movement and camera parameters
        self.move_step = 0.5
        self.forward_speed = 0.1
        self.camera_step = 0.5
        self.zoom_step = 1.0

    def update(self, task):
        # Move the jet forward
        self.jet.setY(self.jet, self.forward_speed)

        # Handle jet movements
        if self.keys["left"]:
            self.jet.setX(self.jet, -self.move_step)
        if self.keys["right"]:
            self.jet.setX(self.jet, self.move_step)
        if self.keys["up"]:
            self.jet.setZ(self.jet.getZ() + self.move_step)
        if self.keys["down"]:
            self.jet.setZ(self.jet.getZ() - self.move_step)
        if self.keys["forward"]:
            self.jet.setY(self.jet, self.move_step)
        if self.keys["backward"]:
            self.jet.setY(self.jet, -self.move_step)

        # Handle speed adjustments
        if self.keys["increase_speed"]:
            self.forward_speed += 0.01
        if self.keys["decrease_speed"]:
            self.forward_speed = max(0, self.forward_speed - 0.01)

        # Update camera position
        update_camera(self)

        return task.cont

app = MyApp()
app.run()
